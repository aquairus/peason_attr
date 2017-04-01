#!/usr/bin/env python

import sys
import os

#       1      0        1     1       1       1
items=[[0,1],[24,30],[63,75],[75,83],[83,92],[51,55],[1,4],[4,7],[15,24],[30,35],[51,55],[35,43]]
for item in items:
     os.system('./train_vgg_s_rap_1.sh {0} {1}'.format(item[0],item[1]))
