#!/usr/bin/env python

import sys
import os


items=[[1,4],[4,7],[15,24],[24,30],[30,35],[34,51],[63,75],[75,83],[83,92]]
for item in items:
    os.system('./train_vgg_s_rap_0.sh {0} {1}'.format(item[0],item[1])
