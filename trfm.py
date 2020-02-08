#!/usr/bin/env python
# --------------------------------------------------------------------------------------
# TRFM is written by @febrifahmi :c 2020
# Toll Road Flood Monitoring system for Indonesia toll road crossdrain flood monitoring
# using OpenCV
# trfm.py : base code for the TRFM analysis.
# --------------------------------------------------------------------------------------

import cv2
import math
import numpy as np 
from matplotlib import pyplot as plt 

himawaribase = 'https://www.data.jma.go.jp/mscweb/data/himawari/img/se3/'
