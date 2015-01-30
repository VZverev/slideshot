# -*- coding: utf-8 -*- 
from django.contrib import admin
from broadcasts.models import Channel, Broadcasting, Slide
# Register your models here.
admin.site.register(Channel)
admin.site.register(Broadcasting)
admin.site.register(Slide)