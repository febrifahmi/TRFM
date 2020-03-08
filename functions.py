#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------
# TRFM is written by @febrifahmi and fiddin alhaz :c 2020
# Toll Road Flood Monitoring system for Indonesia toll road crossdrain flood monitoring
# using OpenCV
# functions.py : code for base image processing.
# --------------------------------------------------------------------------------------

import cv2
import re
import numpy as np
import matplotlib.pyplot as plt
import os
import requests
from datetime import datetime,timedelta
from PIL import Image

# get datetime and time now in UTC and GMT
def gettargettime():
	targetdatetime = datetime.utcnow() - timedelta(minutes=10)
	formatteddatetime = targetdatetime.strftime("%Y-%m-%d %H:%M:%S")
	formattedtime = targetdatetime.strftime("%H%M")
	targetgmttime = datetime.now() - timedelta(minutes=10)
	formattedtimeGMT = targetgmttime.strftime("%H:%M:%S")
	return formatteddatetime, formattedtime, formattedtimeGMT

# i'm using se3 hrp here, means "South East Asia 3 area" - "Heavy Rainfall Potential"
himawaribase = 'https://www.data.jma.go.jp/mscweb/data/himawari/img/se3'
imagename = "/se3_hrp_" + "{}" .format(gettargettime()[1]) + ".jpg"
downloadURL = himawaribase + imagename

# set saved image folder
imgfolder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'images'))
savedimgname = imgfolder + imagename

# download himawari sat image
def downloadhimawari():
	with open(savedimgname, 'wb') as f:
	    f.write(requests.get(downloadURL).content)
	    f.close()

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

# set color to extract from himawari map. green to extract map, and pink/light purple to extract hrp area. width of image 1101x501 pixels
clrmap = '(0, 255, 0, 255)'
# maskhrp = cv2.inRange(hsv_nemo, light_orange, dark_orange)
clrhrp1 = '(255, 0, 170, 255)'
clrhrp2 = '(255, 0, 180, 255)'
clrhrp3 = '(255, 0, 190, 255)'
clrhrp4 = '(255, 0, 200, 255)'

# get pixels which has green color to extract the map/islands, and pink/light purple to extract the hrp area
immapfile = '/basemap.png'
immappath = imgfolder + immapfile
hrpmapfile = '/currenthrpmap.png'
hrpmappath = imgfolder + hrpmapfile

# to do: change the module used to OpenCV
def getmaphimawari():
	# create empty image with width 1101x501 pixels
	im = Image.new('RGBA', (1101, 501))
	for x in range(1101):
		for y in range(501):
			im.putpixel((x,y),(0, 0, 0, 255))

	# open and check all pixels from the himawari sat image
	himsatimg = Image.open(savedimgname) 
	for x in range(1101):
		for y in range(501):
			imgmap = himsatimg.getpixel((x,y))
			if imgmap == clrmap:
				# paint the map
				im.putpixel((x,y),clrmap)
	im.save(immappath)
	print("Basemap created.")

# using opencv instead of PIL to get basemap of islands from himawari satimage
def cv_getmaphimawari():
	# read the image and convert as hsv color
	im = cv2.imread(savedimgname, cv2.IMREAD_UNCHANGED)
	# im_hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
	# 
	rgb_color1 = np.asarray([0, 0, 255])   # white!
	rgb_color2 = np.asarray([0, 255, 0])   # green! note the order
	#
	mask = cv2.inRange(im, rgb_color1, rgb_color2)
	#
	plt.im(mask, cmap='gray')   # this colormap will display in black / white
	plt.show()


# get pixels which has pink/magenta color to extract the heavy rainfall potential area
def getmaphrp(selectedimg):
	# create empty image with width 1101x501 pixels
	im = Image.new('RGBA', (1101, 501))
	for x in range(1101):
		for y in range(501):
			im.putpixel((x,y),(0, 0, 0, 255))

	# open and check all pixels from the himawari sat image
	himsatimg = Image.open(selectedimg)
	for x in range(1101):
		for y in range(501):
			imgmap = himsatimg.getpixel((x,y))
			if imgmap == clrhrp1 or imgmap == clrhrp2 or imgmap == clrhrp3 or imgmap == clrhrp4:
				# paint the map
				im.putpixel((x,y),clrhrp1)
	im.save(hrpmappath)
	print("Current HRP map created.")

# read all files in folder and select which one shold be processed
def selectimg2process():
	for file in os.listdir(imgfolder):
	    file_path = os.path.join(imgfolder, file)
	    if 'se3_hrp_' in file_path:
		    try:
		        if os.path.isfile(file_path) or os.path.islink(file_path):
		            print(file)
		        elif os.path.isdir(file_path):
		            print(file,' (directory)')
		    except Exception as e:
		        print('Error reading %s. Reason: %s' % (file_path, e))
	    else:
	    	print('No himawari satellite image found in folder. Pass...')
	# pause and create selection dialog
	selection = input('Please select the image (number) you want to process: ')
	if re.search('\d+',selection):
		print('Processing image #',selection)
		getmaphrp(selection)