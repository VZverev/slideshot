# -*- coding: utf-8 -*- 
from django.db import models

# model of Channel
class Channel(models.Model):
    owner = models.ForeignKey(User, verbose_name='Владелец', related_name="channels")
    members = models.ManyToManyField(User, verbose_name="Участники", related_name="membership")
    title = models.CharField(u'Заголовок', max_length=200)
    desc = models.TextField(u'Описание', max_length = 10000)
    public_channel = models.BooleanField(u'Is public channel?', default=True)
    def __str__(self):
        return self.title

# model of Broadcasting
class Broadcasting(models.Model):
    title = models.CharField(u'Заголовок', max_length=40)
    desc = models.TextField(u'Описание', max_length = 10000)
    channel = models.ForeignKey(Channel, verbose_name='Канал', related_name="broadcasts")#relation to channel
    start_date = models.DateTimeField(u'Дата и время начала',auto_now_add=True)
    tags = models.CharField(max_length=10)
    active = models.BooleanField(u'Активна сейчас?', default=False)
    #???можно будет добавить количество просмотров презентации
    def __str__(self):
        #privacy added for debug
        if self.channel.public_channel:
            privacy = 'Public'
        else:
            privacy = 'Private'
        return self.title + '[' + privacy + ']'
    
# model of Slide
class Slide(models.Model):
    file = models.FileField(upload_to=self.get_upload_path)
    broadcasting = models.ForeignKey(Broadcasting, related_name="slides")#relation to broadcasting
    position = models.IntegerField()#slide's position in presentation
    dt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.broadcasting.__str__()+" #"+self.position.__str__()
    
    def get_upload_path(self, filename):
        if self and self.broadcasting and self.broadcasting.channel and self.position:
            return 'slides/'+self.broadcasting.channel.title+'_'+self.broadcasting.title+'/'+'%s_%s%s' % (filename[:filename.rfind('.')] , self.position, filename[filename.rfind('.'):]) 
        else:
            return 'slides/images/%s_%s%s' % (filename[:filename.rfind('.')] , get_random_string(length=4), filename[filename.rfind('.'):]) 
    

    