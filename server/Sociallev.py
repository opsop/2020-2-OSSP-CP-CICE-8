from hotKeyword import *
import os

DB_PATH = os.path.dirname(__file__) + '/CoronaBotDB'

'''
기본적으로 level이라는 entity를 받으면 실행
'''

'''
lev 엔티티 (필수 파라미터)
: 되묻기 질문으로 받아오는 애
단계별 특징, 지역별 단계 보기
'''

'''
단계별 기준 및 방역조치
다중 이용 시설
일상 및 사회, 경제적 활동
'''

'''
지역별 단계는
http://ncov.mohw.go.kr/duBoardList.do?brdId=2&brdGubun=29&flowId=main
의 자료 활용

크롤링이 막혀있지만, 자료 이용자체는 가능해서
이미지 url을 주기적으로 수작업으로 업데이트 예정
'''

# f = open(DB_PATH + '/distance.txt', 'r')
# line = f.readline()
# f.close()
# line = '"'+line+'"'

'''
그냥 url 파싱해오는게 서버에서 돌렸을때 에러 뜨는 부분이 있을수도 있더라고요 ㅠㅠ
계속 안돌아가면 그냥 이걸로 합시다...
저 단계별 특징 answer에 이게 들어가면 되요
(아래꺼)

answer = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": "http://ncov.mohw.go.kr/duBoardList.do?brdId=2&brdGubun=29&flowId=main"
                            }
                        }
                    ]
                }
            }
'''

def level(param):
    hotKeyword("사회적 거리두기 단계")
    if param == "단계별 특징":
        answer = {
          "version": "2.0",
          "template": {
            "outputs": [
              {
                "listCard": {
                  "header": {
                    "title": "궁금한 항목을 선택해 주세요."
                  },
                  "items": [
                    {
                      "title": "단계별 기준 및 방역조치",
                      "imageUrl": "https://postfiles.pstatic.net/MjAyMDExMDJfMTYy/MDAxNjA0MzA4NjQxNTA4.f8Lhf1HK0xj8Cml6TUuWUn97uGnL6mYaMgy57shor90g.bUbQz87HsJysMRW9C-WgkMEcLFNYDjUhd8MMuwr8ejMg.PNG.mohw2016/1.png?type=w966",
                      "link": {
                        "web": "https://postfiles.pstatic.net/MjAyMDExMDJfMTYy/MDAxNjA0MzA4NjQxNTA4.f8Lhf1HK0xj8Cml6TUuWUn97uGnL6mYaMgy57shor90g.bUbQz87HsJysMRW9C-WgkMEcLFNYDjUhd8MMuwr8ejMg.PNG.mohw2016/1.png?type=w966"
                      }
                    },
                    {
                      "title": "다중 이용 시설 제한",
                      "imageUrl": "https://postfiles.pstatic.net/MjAyMDExMDJfMTIz/MDAxNjA0MzA4NjQxNTA4.X3Iyw7TMvnglAeHzBIPidOdWV3B2G3_InsZTzfngiaog.g71g0L4ZyBX9jUR6n8O8G_bF5XON3ZJ8NyBPg8HtyUkg.PNG.mohw2016/2.png?type=w966",
                      "link": {
                        "web": "https://postfiles.pstatic.net/MjAyMDExMDJfMTIz/MDAxNjA0MzA4NjQxNTA4.X3Iyw7TMvnglAeHzBIPidOdWV3B2G3_InsZTzfngiaog.g71g0L4ZyBX9jUR6n8O8G_bF5XON3ZJ8NyBPg8HtyUkg.PNG.mohw2016/2.png?type=w966"
                      }
                    },
                    {
                      "title": "일상 및 사회, 경제적 활동 제한",
                      "imageUrl": "https://postfiles.pstatic.net/MjAyMDExMDJfMjg2/MDAxNjA0MzA4NjQxNTEy.TXdorraJiWE8BjeuS4ou-VOqdeFEoIerBzqDRloMRcog.5W8ZCH-TAdxeph7GjBLFn5Ew-QsXOWaDoKRr5KBsHkQg.PNG.mohw2016/3.png?type=w966",
                      "link": {
                        "web": "https://postfiles.pstatic.net/MjAyMDExMDJfMjg2/MDAxNjA0MzA4NjQxNTEy.TXdorraJiWE8BjeuS4ou-VOqdeFEoIerBzqDRloMRcog.5W8ZCH-TAdxeph7GjBLFn5Ew-QsXOWaDoKRr5KBsHkQg.PNG.mohw2016/3.png?type=w966"
                      }
                    }
                  ]
                }
              }
            ]
          }
        }
        return answer

    else:
        answer = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "궁금한 항목을 선택해 주세요."
                        },
                        "items": [
                            {
                                "title": "지역별 사회적 거리두기 단계",
                                "imageUrl": "https://media.vlpt.us/images/i-zro/post/8918b4fd-e489-4a18-8181-94fc2835be71/image.png",
                                "link": {
                                    "web": "http://ncov.mohw.go.kr/duBoardList.do?brdId=2&brdGubun=29&flowId=main"
                                }
                            },
                            {
                                "title": "지역별 사회적 거리두기 단계 뉴스",
                                "imageUrl": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA4MjRfMTg3%2FMDAxNTk4MjQ2NjcyMzU3.61epWupfiorJmHSA8aAKTlm0sKXcxydzKDglZVca568g.3z4bGuxALC3XOVQJnYpnIm2lejRUOfgTbMO4r4k3J5cg.JPEG.jhsarang1893%2F%25BB%25E7%25C8%25B8%25C0%25FB%25B0%25C5%25B8%25AE%25B5%25CE%25B1%25E22%25B4%25DC%25B0%25E815.jpg&type=sc960_832",
                                "link": {
                                    "web": f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={'지역별+사회적+거리두기+단계'}"
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
        return answer