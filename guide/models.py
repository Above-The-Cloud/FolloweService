from django.db import models

# Create your models here.
from django.utils import timezone


class Guide(models.Model):
    username = models.CharField(max_length=100,default='杭州小e')
    avatar = models.CharField(max_length=500,default='http://followe.yiwangchunyu.wang/media/system/ehangzhou.jpg')
    position = models.CharField(max_length=100,default='浙江-杭州')
    title = models.CharField(max_length=100)
    content = models.TextField()
    cover = models.CharField(max_length=500)
    link = models.CharField(max_length=500,default='',blank=True,null=True)
    liked = models.IntegerField(default=0, blank=True,null=True)
    ctime = models.DateTimeField(default = timezone.now)
    mtime = models.DateTimeField(auto_now=True)