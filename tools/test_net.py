#!/usr/bin/env python

# --------------------------------------------------------------------
# This file is part of
# Weakly-supervised Pedestrian Attribute Localization Network.
#
# Weakly-supervised Pedestrian Attribute Localization Network
# is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Weakly-supervised Pedestrian Attribute Localization Network
# is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Weakly-supervised Pedestrian Attribute Localization Network.
# If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------

import _init_path

import argparse
import os
import pprint
import sys
import time

import caffe
from wpal_net.config import cfg, cfg_from_file, cfg_from_list
from wpal_net.test import test_net
from caffe.proto import caffe_pb2
from google.protobuf import text_format

def parse_args():
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser(description='test WPAL-network')
    parser.add_argument('--gpu', dest='gpu_id',
                        help='GPU device ID to use (default: -1)',
                        default=-1, type=int)
    parser.add_argument('--def', dest='prototxt',
                        help='prototxt file defining the network',
                        default=None, type=str)
    parser.add_argument('--net', dest='caffemodel',
                        help='model to test',
                        default=None, type=str)
    parser.add_argument('--start', dest='start',
                        help='Attribute index',
                        default=0, type=int)
    parser.add_argument('--end', dest='end',
                        help='Attribute index',
                        default=92, type=int)
    parser.add_argument('--cfg', dest='cfg_file',
                        help='optional cfg file', default=None, type=str)
    parser.add_argument('--wait', dest='wait',
                        help='wait until net file exists',
                        default=True, type=bool)
    parser.add_argument('--set', dest='set_cfgs',
                        help='set cfg keys', default=None,
                        nargs=argparse.REMAINDER)
    parser.add_argument('--db', dest='db',
                        help='the name of the database',
                        default=None, type=str)
    parser.add_argument('--setid', dest='par_set_id',
                        help='the index of training and testing data partition set',
                        default='0', type=int)
    parser.add_argument('--outputdir', dest='output_dir',
                        help='the directory to save outputs',
                        default='./output', type=str)

    args = parser.parse_args()

    if args.prototxt is None or args.caffemodel is None or args.db is None:
        parser.print_help()
        sys.exit()

    return args


if __name__ == '__main__':
    args = parse_args()

    print('Called with args:')
    print(args)

    if args.cfg_file is not None:
        cfg_from_file(args.cfg_file)
    if args.set_cfgs is not None:
        cfg_from_list(args.set_cfgs)

    cfg.GPU_ID = args.gpu_id

    print('Using cfg:')
    pprint.pprint(cfg)

    while not os.path.exists(args.caffemodel) and args.wait:
        print('Waiting for {} to exist...'.format(args.caffemodel))
        time.sleep(10)

    # set up Caffe
    if args.gpu_id == -1:
        caffe.set_mode_cpu()
    else:
        caffe.set_mode_gpu()
        caffe.set_device(args.gpu_id)


    start=args.start
    end=args.end
    num_attr=end-start


    net_file=args.prototxt
    n=caffe_pb2.NetParameter()
    text_format.Merge(open(net_file).read(), n)
    n.layer[-6].inner_product_param.num_output=num_attr

    new_dir=os.path.dirname(net_file)+"/train_net_dir"
    new_file=  new_dir+"/test_net_{}_{}.prototxt".format(start,end)

    with open(new_file,'w+') as  new_prototxt_file:
        new_prototxt_file.write(unicode(text_format.MessageToString(n)))

    args.prototxt=new_file
    # print args.prototxt
    # print num_attr
    # time.sleep(10)
    net = caffe.Net(new_file, args.caffemodel, caffe.TEST)
    net.name = os.path.splitext(os.path.basename(args.caffemodel))[0]

    if args.db == 'RAP':
        """Load RAP database"""
        from utils.rap_db import RAP
        db = RAP(os.path.join('data', 'dataset', args.db), args.par_set_id)
    else:
        """Load PETA dayanse"""
        from utils.peta_db import PETA
        db = PETA(os.path.join('data', 'dataset', args.db), args.par_set_id)

    db.label_weight=db.label_weight[start:end]
    db.labels=db.labels[:,start:end]
    db.num_attr=num_attr

    args.output_dir=args.output_dir+"/attr{}_{}".format(start,end)
    try:
        os.makedirs(args.output_dir)
    except:
        pass


    test_net(net, db, args.output_dir)
