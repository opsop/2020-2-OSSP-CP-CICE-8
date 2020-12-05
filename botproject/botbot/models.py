from django.db import models

# Create your models here.
class StatisticValues(models.Model):
    # 지역별 감염 정보 외의, 전체 감염 정보 / 검사완료 & 검사중 등 다른 통계 자료를 저장하는 테이블

    updateTime = models.CharField(max_length=15, default="2020.11.21", primary_key=True) # 정보 업데이트 시간 data['updateTime'][23:28] -> 월.일(00.00 구조)
    TotalCase = models.TextField(default="0")            # 총 확진자
    TotalDeath = models.TextField(default="0")           # 총 사망자
    TotalRecovered = models.TextField(default="0")       # 총 완치자
    NowCase = models.TextField(default="0")              # 치료중인 사람
    TotalChecking = models.TextField(default="0")        # 검사완료
    # notcaseCount = models.TextField(default="0")         # 결과 음성

    TodayCase = models.TextField(default="0")            # 전일 대비 확진자, data2["data0_1"]의미
    TodayRecovered = models.TextField(default="0")       # 전일 대비 완치자

# from django.db import models
# from botbot.models import StatisticValues

    def __str__(self):
        return self.updateTime