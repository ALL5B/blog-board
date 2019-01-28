from django.db import models
from django.utils import timezone
# Create your models here.


class Junle(models.Model):
    name= models.CharField('ジャンル名',max_length=255)
    created_at = models.DateTimeField('作成日',default=timezone.now)

    def __str__(self):
        return self.name


class Board(models.Model):
    title = models.CharField('タイトル名',max_length=50)
    text = models.TextField('説明文')
    created_at = models.DateTimeField('作成日',default=timezone.now)
    junle = models.ForeignKey(Junle,verbose_name="ジャンル",on_delete=models.PROTECT,default=1)
    def __str__(self):
        return self.title




class Chat(models.Model):
    name = models.CharField('お名前',max_length=10,default="名無し")
    text = models.TextField('本文')
    board = models.ForeignKey(Board,verbose_name="スレッド",on_delete=models.PROTECT)
    created_at = models.DateTimeField('作成日',default=timezone.now)

    def __str__(self):
        return self.text[:10]
