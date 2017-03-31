#!/usr/bin/env python

import sys
import os


items=[[63,75]]
#[0,1],[24,30],
# ,[75,83],[83,92],[51,55],[1,4],[4,7],[15,24],[30,35],[51,55],[35,43]]
for item in items:
    os.system('mv  /data/my_rap_network/data/snapshots/VGG_S_MLL_RAP/0/attr{0}_{1}/RAP/vgg_s_mll_rap_iter_10000.caffemodel  /data/my_rap_network/data/snapshots/VGG_S_MLL_RAP/0/attr{0}_{1}/RAP/result_10000.caffemodel'.format(item[0],item[1]))


for item in items:
    os.system("mv /data/my_rap_network/output/attr{0}_{1}/acc.txt /data/my_rap_network/output/attr{0}_{1}/old_acc.txt".format(item[0],item[1]))
