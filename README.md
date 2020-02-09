# Toll Road Flood Monitoring (TRFM)

Toll Road Flood Monitoring (TRFM) system is a system developed to monitor flood occurences around crossdrain of Indonesia's toll roads.

This system utilized available satellite image data and toll road CCTV data stream derive approximation of puddle/inundation on toll road near crossdrain.

## Toll Road Flood Monitoring System design flow:

### 1. Read Himawari real time satellite images periodically. 

Normally data.jma.go.jp updates data automatically every 10 minutes. We read the data by creating image object from the url of the image such as: `https://www.data.jma.go.jp/mscweb/data/himawari/img/se3/se3_hrp_0340.jpg`

> **se3** -> South East Asia 3

> **hrp** -> heavy rainfall potential

> **0340** -> the timestamp of the image

So, we basically need to construct the base url and the file url, donwload the image a couple seconds after the time variable reached, and analyze it.

The `trfm.py` script is run using cron every 10 minute.

Code of `getdata.sh`:
`
#!/bin/bash
source /home/febrifahmi/Documents/01_CODING/TRFM/bin/activate
python /home/febrifahmi/Documents/01_CODING/TRFM/trfms/TRFM/trfm.py
`

### 2. Analyze the image

1. Set pixels coordinate that represents the location of cities in himawari satellite image;
2. Read specific color (deep pink-purple which represent heavy rainfall areas) and check if it's coincide with the location of cities;
3. if yes, we load and check for the data of the toll road crossdrain location in that city;
4. from the video stream, we take a screnshot/extract image and try to detect the puddle/inundation. we could use opencv and apply several methods, e.g edge canny detection combined with object detection to check if there is a slower movement of cars in the area of the puddle/inundation. if yes, send alert.

### 3. (to do next)
