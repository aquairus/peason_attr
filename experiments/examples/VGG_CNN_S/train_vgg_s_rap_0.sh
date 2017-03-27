#!/usr/bin/env bash
cd `dirname "${BASH_SOURCE[0]}"`/../../..
start=$1
end=$2
./experiments/scripts/wpal_net.sh 0 VGG_S_MLL_RAP data/pretrained/VGG_CNN_S.caffemodel   RAP 0 ${start} ${end} --set TRAIN.BATCH_SIZE 45
