import datetime
from django.db import models

# Create your models here.
class User(models.Model):
    '''用户数据模型'''

    SEX = (
        ('男','男'),
        ('女','女'),
    )
    nickname = models.CharField(max_length=32, unique=True)
    phonenum = models.CharField(max_length=16, unique=True)

    sex = models.CharField(max_length=8, choices=SEX)
    avatar = models.CharField(max_length=256)       #头像
    location = models.CharField(max_length=32)

    birth_year = models.IntegerField()
    birth_month = models.IntegerField()
    birth_day = models.IntegerField()

    @property
    def age(self):
        today = datetime.date.today()
        birth_date = datetime.date(self.birth_year,self.birth_month,self.birth_day)
        return (today - birth_date).days // 365

class Profile(models.Model):
    '''用户配置项'''

    SEX = (
        ('男', '男'),
        ('女', '女'),
    )
    dating_sex = models.CharField(max_length=8, choices=SEX, verbose_name='匹配的性别')
    location = models.CharField(max_length=32, verbose_name='目标城市')

    min_distance = models.IntegerField(default=1, verbose_name='最小查找范围')
    max_distance = models.IntegerField(default=10, verbose_name='最大查找范围')

    min_dating_age = models.IntegerField(default=18, verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=45, verbose_name='最大交友年龄')

    vibration = models.BooleanField(default=True, verbose_name='开启震动')
    only_matche = models.BooleanField(default=True, verbose_name='不让匹配的人看我的相册')
    auto_play = models.BooleanField(default=True, verbose_name='自动播放视频')