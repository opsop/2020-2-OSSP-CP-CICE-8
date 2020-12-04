[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat-square)](#contributors-)
# 2020-2-OSSP-CP-CICE-8
[데이터사이언스 연계전공]Team_CICE

## Member

* [유영현](https://github.com/0hyunU)
* [권나영](https://github.com/i-zro)
* [송승민](https://github.com/SeungMinSong2929)
* [문소연](https://github.com/opsop)

## About
[Corona-Tracker API](https://github.com/Kamaropoulos/COVID19Py/blob/master/README.md#about) 활용 코로나 챗봇.

## 

### Installation
1. Clone git repository
```
git clone https://github.com/CSID-DGU/2020-2-OSSP-CP-CICE-8.git
cd server
```

2. Install required packages
Linux Terminal / Windows cmd, PowerShell / Git bash
```
sudo apt install python3-pip #install pip
python3 -m pip install --upgrade pip
pip install Flask
pip install COVID19Py
pip install bs4
pip install requests
pip3 install matplotlib
```
3. run server
```
python chatbot.py runserver
```
```
http://0.0.0.0:5000/ -> http://ip-address:5000/ 
```
use your own ip-address


## Bot Diagram
![diagram](bot_monitoring/bot_diagram.png)
