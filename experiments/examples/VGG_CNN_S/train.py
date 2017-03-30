#!/usr/bin/env python

import sys
import os


items=[[35,43],[51,55]]
for item in items:
    os.system('./train_vgg_s_rap_0.sh {0} {1}'.format(item[0],item[1]))
