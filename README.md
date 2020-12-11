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
* 카카오 오픈빌더를 활용하여 개발한 코로나 챗봇.
* 카카오톡에 "코로나 챗봇" 채널 친구를 통해 확인 가능.

## Want to chat with our chatbot?
➡ [Click Here](https://pf.kakao.com/_KgxlnK)

## Used APIs
[chatbot_organization.md](https://github.com/CSID-DGU/2020-2-OSSP-CP-CICE-8/blob/main/chatbot_organization.md)에 안내.

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
pip install apscheduler
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
![diagram](bot_monitoring/bot_diagram_final.png)

*** 

## Bot images
1. 국내 현황 보기 <br>
    ![01_국내현황보기](bot_monitoring/bot_image/01_국내현황보기.jpg) <br>
<br>

2. 국내 현황 추이 그래프 <br>
    ![02_국내현황추이그래프](bot_monitoring/bot_image/02_국내현황추이그래프.jpg) <br>
<br>

3. 선별진료소 안내 <br>
    ![03_선별진료소](bot_monitoring/bot_image/03_선별진료소.jpg) <br>
<br>

4. 사회적 거리두기 단계 <br>
    * 단계별 특징 <br>
    ![04_사회적거리두기_단계별특징](bot_monitoring/bot_image/04_사회적거리두기_단계별특징.jpg) <br> <br>

    * 지역별 단계보기 <br>
    ![04_사회적거리두기_지역별단계보기](bot_monitoring/bot_image/04_사회적거리두기_지역별단계보기.jpg) <br>
<br>

5. 인기 키워드 <br>
    <img src="/bot_monitoring/bot_image/05_인기키워드.jpg" width="40%" height ="15%">
<br>

6. 하단에 검색어 선택 기능 <br>
    ![06_하단에검색어선택](bot_monitoring/bot_image/06_하단에검색어선택.jpg) <br>
<br>

7. 전세계 현황 보기 <br>
    ![07_전세계현황](bot_monitoring/bot_image/07_전세계현황.jpg) <br>
<br>

8. 네이버/ 유투브 뉴스 제공 기능 <br>
    * 네이버 뉴스 <br>
    ![08_네이버뉴스](bot_monitoring/bot_image/08_네이버뉴스.jpg) <br> <br>

    * 유투브 뉴스 <br>
    ![08_유투브뉴스](bot_monitoring/bot_image/08_유투브뉴스.jpg) <br>
<br>

9. 재난 문자 보기 <br>
    ![09_재난문자](bot_monitoring/bot_image/09_재난문자.jpg) <br>
<br>

10. 자가진단 문진표 제공 <br>
    <img src="bot_monitoring/bot_image/10_자가진단.jpg" width="40%" height ="10%"/>
    <br>
<br>

11. 근처 병원 및 약국 안내 <br>
    ![11_근처병원및약국](bot_monitoring/bot_image/11_근처병원및약국.jpg) <br>
<br>

