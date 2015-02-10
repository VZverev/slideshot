# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response, redirect 
from django.template import RequestContext
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from broadcasts.models import Channel, Broadcasting, Slide
from broadcasts.serializers import SlideSerializer, SlideGetSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from broadcasts.permissions import UserPermission


#for testing ajax 
def slider(request, bk = 0):
    try:
        broadcasting = Broadcasting.objects.get(pk=int(bk))
    except Broadcasting.DoesNotExist:
        raise Http404
    slides = broadcasting.slides.all()
    html = render_to_response('slider.html', {'slides': slides }, context_instance=RequestContext(request))
    return HttpResponse(html)

#api for slide uploading
class SlideViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer
    
#api for taking slides
class SlideGet(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = (UserPermission,)
    
    def get_object(self, bk, pos):
        try:
            broadcasting = Broadcasting.objects.get(pk=int(bk))
        except Broadcasting.DoesNotExist:
            raise Http404
        slides = broadcasting.slides.all()
        try:
            return slides.get(position=int(pos))
        except Slide.DoesNotExist:
            raise Http404

    def post(self, request,format=None):
        bk = request.data.get('bk')
        pos = request.data.get('pos')
        slide = self.get_object(bk,pos)
        serializer = SlideGetSerializer(slide)
        return Response(serializer.data)

#sign up and sign in or login as anonimus
#redirect to mainpage
'''def hellopage(request):
    pass

#TODO: уточнить у светы, пока что ничего
def mainpage(request):
    pass'''
#список доступных пользователю каналов
def channel_list(request):
    if not request.user.is_authenticated():
        channels = Channel.objects.all(public_channel=True)
    
    html = render_to_response('channel_list.html', {'channels': channels }, context_instance=RequestContext(request))
    return HttpResponse(html)

#список доступных пользователю каналов
def broadcasting_list(request):
    broadcastings = Broadcasting.objects.all()
    
    html = render_to_response('broadcasting_list.html', {'broadcastings': broadcastings }, context_instance=RequestContext(request))
    return HttpResponse(html)

#презентация (слайды описание, доп даныне связанные с ней)
def broadcasting(request, id):
    broadcasting = Broadcasting.objects.get(pk=id)
    
    html = render_to_response('broadcasting.html', {'broadcasting': broadcasting }, context_instance=RequestContext(request))
    return HttpResponse(html)

#канал (доступные презентации, описание канала)
#для владельца возможность редактирования данных
def channel(request, id):
    channel = Channel.objects.get(pk=id)
    
    html = render_to_response('channel.html', {'channel': channel }, context_instance=RequestContext(request))
    return HttpResponse(html)
    
# redirect на канал пользователя channel(id)
def mycabinet(request):
    if not request.user.is_authenticated():
        return redirect('/')
