from hotKeyword import *

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

    answer = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleImage": {
                    "imageUrl": "http://ncov.mohw.go.kr/front_new/modules/img_view.jsp?img_loc=/upload/mwEditor/202012/1607080506682_20201204201506.png",
                    "altText": "보물상자입니다"
                }
            }
        ]
        }
        }
    return answer
