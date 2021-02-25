import datetime
from django.db import models

# Create your models here.
class User(models.Model):
    SEX = (
        ('男','男'),
        ('女','女'),
    )
    nickname = models.CharField(max_length=32, unique=True)
    phonenum = models.CharField(max_length=16, unique=True)

    sex = models.CharField(max_length=8, choices=SEX)
    birth_year = models.IntegerField()
    birth_month = models.IntegerField()
    birth_day = models.IntegerField()
    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=32)

    @property
    def age(self):
        today = datetime.date.today()
        birth_date = datetime.date(self.birth_year,self.birth_month,self.birth_day)
        return (today - birth_date).days // 365

