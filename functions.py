#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------
# TRFM is written by @febrifahmi :c 2020
# Toll Road Flood Monitoring system for Indonesia toll road crossdrain flood monitoring
# using OpenCV
# functions.py : code for base image processing.
# --------------------------------------------------------------------------------------

from datetime import datetime,timedelta

# get datetime and time now in UTC and GMT
def gettargettime():
	targetdatetime = datetime.utcnow() - timedelta(minutes=10)
	formatteddatetime = targetdatetime.strftime("%Y-%m-%d %H:%M:%S")
	formattedtime = targetdatetime.strftime("%H%M")
	targetgmttime = datetime.now() - timedelta(minutes=10)
	formattedtimeGMT = targetgmttime.strftime("%H:%M:%S")
	return formatteddatetime, formattedtime, formattedtimeGMT

# to do:
# buat fungsi delete old sat images untuk menghemat space
# 