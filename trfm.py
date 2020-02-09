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

print(fn.downloadURL)
print(fn.gettargettime()[2])
print(fn.imgfolder)
fn.downloadhimawari()


# read the last/current satellite image using numpy
# img = cv2.imread('a.jpg',0)


# check if the time reach 00:03:00 and clean the images in folder
fn.clearimgfolder()