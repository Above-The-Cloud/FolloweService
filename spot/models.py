from django.db import models

# Create your models here.
from django.utils import timezone


class Spot(models.Model):
    province = models.CharField(max_length=100)#省份信息
    city = models.CharField(max_length=100)#城市信息
    name = models.CharField(max_length=100)#景点名
    address = models.CharField(max_length=100)#详细地址
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)#至少价格
    mark = models.DecimalField(default=4.7, decimal_places=2, max_digits=10)#景点评分
    pic_url = models.CharField(max_length=200)#景点图片url
    level = models.CharField(max_length=100, )#景点级别
    ctime = models.DateTimeField(default = timezone.now)
    mtime = models.DateTimeField(auto_now=True)