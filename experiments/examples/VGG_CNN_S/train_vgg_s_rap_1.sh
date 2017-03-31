#!/usr/bin/env bash
cd `dirname "${BASH_SOURCE[0]}"`/../../..
start=$1
end=$2


./experiments/scripts/wpal_net.sh 0 VGG_S_MLL_RAP ./data/snapshots/VGG_S_MLL_RAP/0/attr"${start}"_"${end}"/RAP/result_10000.caffemodel   RAP 0 ${start} ${end} --set TRAIN.BATCH_SIZE 45
