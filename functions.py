#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------
# TRFM is written by @febrifahmi :c 2020
# Toll Road Flood Monitoring system for Indonesia toll road crossdrain flood monitoring
# using OpenCV
# functions.py : code for base image processing.
# --------------------------------------------------------------------------------------

import os
import requests
from datetime import datetime,timedelta

# get datetime and time now in UTC and GMT
def gettargettime():
	targetdatetime = datetime.utcnow() - timedelta(minutes=10)
	formatteddatetime = targetdatetime.strftime("%Y-%m-%d %H:%M:%S")
	formattedtime = targetdatetime.strftime("%H%M")
	targetgmttime = datetime.now() - timedelta(minutes=10)
	formattedtimeGMT = targetgmttime.strftime("%H:%M:%S")
	return formatteddatetime, formattedtime, formattedtimeGMT

# i'm using se3 hrp here, means "South East Asia 3 area" - "Heavy Rainfall Potential"
himawaribase = 'https://www.data.jma.go.jp/mscweb/data/himawari/img/se3/'
imagename = "/se3_hrp_" + "{}" .format(gettargettime()[1]) + ".jpg"
downloadURL = himawaribase + imagename

# set saved image folder
imgfolder = os.path.abspath(os.path.join(os.path.dirname('TRFM'), '..', 'images'))
savedimgname = imgfolder + imagename

# download himawari sat image
def downloadhimawari():
	with open(savedimgname, 'wb') as f:
	    f.write(requests.get(downloadURL).content)

# remove all image files in folder if time reached 00:03:00 UTC (or the next day), so we can start with empty and fresh data
def clearimgfolder():
	if gettargettime()[1] == '0003':
		for file in os.listdir(imgfolder):
		    file_path = os.path.join(imgfolder, file)
		    try:
		        if os.path.isfile(file_path) or os.path.islink(file_path):
		            os.unlink(file_path)
		        elif os.path.isdir(file_path):
		            shutil.rmtree(file_path)
		    except Exception as e:
		        print('Failed to delete %s. Reason: %s' % (file_path, e))
	else:
		print('Not cleaning. Not reached 0003 yet.  Pass.')
		pass

# to do:
# buat fungsi delete old sat images untuk menghemat space
# 