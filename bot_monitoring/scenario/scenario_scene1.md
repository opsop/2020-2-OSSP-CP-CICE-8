<h1> scenario_시나리오01 </h1>

<h3>[시나리오 작성]</h3>
<h3>인기 키워드 </h3>
<b> 사용자 발화 </b><br>
4개 작성<br>
<b> 봇 응답</b><br>
텍스트형 -3위까지 보여줌<br><br>

<h3>유투브 뉴스 </h3>
<b> 사용자 발화 </b><br>
20개 작성<br>
머신러닝 발퐈 28개 작성<br>
<b> 파라미터 설정</b><br>
youtube @youtube 유투브<br>
<b> 봇 응답</b><br>
텍스트형<br>
확진자 정보/ 백신 개발/ 코로나 후유증/ 집단 감염/ 기타 검색 블록 생성<br><br>

<h3>네이버 뉴스 </h3>
<b> 사용자 발화 </b><br>
24개 작성
<b> 파라미터 설정</b><br>
naverNews @naver 네이버 뉴스<br>
<b> 봇 응답</b><br>
텍스트형<br>
확진자 정보/ 백신 개발/ 코로나 후유증/ 집단 감염/ 기타 검색 블록 생성<br><br>

<h3>국내 현황 </h3>
<b> 사용자 발화 </b><br>
14개 작성
<b> 파라미터 설정</b><br>
KoreaSituation @KoreaSituation 국내 현황<br>
<b> 봇 응답</b><br>
텍스트형<br>

```
국내 현황


확진자:

완치자: 

사망자:
```

<br>

<h3>[엔티티 작성]</h3>
<b>youtube</b><br>
<ul>
<li>유투브</li>
<li>기타 검색</li>
<li>집단 감염</li>
<li>코로나 후유증</li>
<li>백신 개발</li>
<li>확진자</li>
</ul><br>

<b>naver</b><br>
<ul>
<li>네이버</li>
<li>기타 검색</li>
<li>집단 감염</li>
<li>코로나 후유증</li>
<li>백신 개발</li>
<li>확진자</li>
</ul><br>

<b>KoreaSituation</b><br>
<ul>
<li>국내</li>
<li>사망자</li>
<li>완치자</li>
<li>확진자</li>
</ul><br>

<h3>[스킬 작성]</h3>
스킬 이름: KoreaData<br>
chatbot.py에서 국내 코로나 데이터 받아와서 출력하는 기능 구현<br>
