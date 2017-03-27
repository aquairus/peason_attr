#!/usr/bin/env bash
cd `dirname "${BASH_SOURCE[0]}"`/../../..
./tools/test_net.py --setid 0 --net ./data/snapshots/VGG_S_MLL_RAP/0/attr0_3/RAP/vgg_s_mll_rap_iter_10000.caffemodel --start 0 --end 1 --def ./models/VGG_S_MLL_RAP/test_net.prototxt --gpu 1 --db RAP
