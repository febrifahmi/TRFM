#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------
# TRFM is written by @febrifahmi :c 2020
# Toll Road Flood Monitoring system for Indonesia toll road crossdrain flood monitoring
# using OpenCV
# trfm.py : base code for TRFM analysis that will be run every 10 minutes using cron
# --------------------------------------------------------------------------------------

import cv2
import math
import numpy as np
from matplotlib import pyplot as plt
import functions as fn

# i'm using se3 hrp here, means "South East Asia 3 area" - "Heavy Rainfall Potential"
himawaribase = 'https://www.data.jma.go.jp/mscweb/data/himawari/img/se3/'
imagename = "se3_hrp_" + "{}" .format(fn.gettargettime()[1]) + ".jpg"
downloadURL = himawaribase + imagename

print(downloadURL)
print(fn.gettargettime()[2])