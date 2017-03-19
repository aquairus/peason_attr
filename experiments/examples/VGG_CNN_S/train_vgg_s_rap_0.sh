#!/usr/bin/env bash
cd `dirname "${BASH_SOURCE[0]}"`/../../..
./experiments/scripts/wpal_net.sh 1 VGG_S_MLL_RAP ./data/snapshots/VGG_S_MLL_RAP/0/RAP/vgg_s_mll_rap_iter_5000.caffemodel  RAP 0 --set TRAIN.BATCH_SIZE 54
