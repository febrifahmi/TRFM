# Toll Road Flood Monitoring (TRFM)

Toll Road Flood Monitoring (TRFM) system is a system developed to monitor flood occurences around crossdrain of Indonesia's toll roads.

## Toll Road Flood Monitoring System design flow:

### 1. Read Himawari real time satellite images periodically. 

Normally data.jma.go.jp updates data automatically every 10 minutes. We read the data by creating image object from the url of the image such as: `https://www.data.jma.go.jp/mscweb/data/himawari/img/se3/se3_hrp_0340.jpg`

> **se3** -> South East Asia 3

> **hrp** -> heavy rainfall potential

> **0340** -> the timestamp of the image

So, we basically need to construct the base url and the file url, donwload the image a couple seconds after the time variable reached, and analyze it.

### 2. (to do next)
