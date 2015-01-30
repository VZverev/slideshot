# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User, Group
from django.utils.crypto import get_random_string

def get_upload_path(instance, filename):
        return '.slides/images/%s_%s%s' % (filename[:filename.rfind('.')] , get_random_string(length=4), filename[filename.rfind('.'):]) 
    
# model of Channel
class Channel(models.Model):
    owner = models.ForeignKey(User, verbose_name=u'Владелец', related_name=u'channels')
    members = models.ManyToManyField(User, verbose_name=u'Участники', related_name=u'membership')
    title = models.CharField(u'Заголовок', max_length=200)
    desc = models.TextField(u'Описание', max_length = 10000)
    public_channel = models.BooleanField(u'Is public channel?', default=True)
    def __unicode__(self):
        return self.title

# model of Broadcasting
class Broadcasting(models.Model):
    title = models.CharField(u'Заголовок', max_length=40)
    desc = models.TextField(u'Описание', max_length = 10000)
    channel = models.ForeignKey(Channel, verbose_name='Канал', related_name=u'broadcasts')#relation to channel
    start_date = models.DateTimeField(u'Дата и время начала',auto_now_add=True)
    tags = models.CharField(max_length=10)
    active = models.BooleanField(u'Активна сейчас?', default=False)
    #???можно будет добавить количество просмотров презентации
    def __unicode__(self):
        #privacy added for debug
        if self.channel.public_channel:
            privacy = 'Public'
        else:
            privacy = 'Private'
        return self.title + '[' + privacy + ']'
    
# model of Slide
class Slide(models.Model):
    file = models.ImageField(upload_to=get_upload_path)
    broadcasting = models.ForeignKey(Broadcasting, related_name=u'slides', verbose_name=u'Презентация')
    position = models.IntegerField(u'Порядковый номер')
    dt_create = models.DateTimeField(u'Дата создания',auto_now_add=True)
    def __unicode__(self):
        return self.broadcasting.__unicode__()+" #"+self.position.__str__()
    