from django.db import models

# Create your models here.
from django.utils import timezone


class Train(models.Model):
    trainno = models.CharField(max_length=100)#列次名称
    start = models.CharField(max_length=100)#起点站
    end = models.CharField(max_length=100)#终点站
    starttime = models.DateTimeField()#发车时间
    endtime = models.DateTimeField()#到达时间
    costtime = models.CharField(max_length=100,default='',blank=True,null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    ctime = models.DateTimeField(default = timezone.now)
    mtime = models.DateTimeField(auto_now=True)