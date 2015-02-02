# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response, redirect 
from django.template import RequestContext
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from broadcasts.models import Broadcasting, Slide
from broadcasts.serializers import SlideSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

def slider(request, id = 0):
    slides = Broadcasting.objects.get(pk=1).slides.all()
    html = render_to_response('slider.html', {'slides': slides }, context_instance=RequestContext(request))
    return HttpResponse(html)

def get_new(request):
    if request.method == 'POST':
        pos = request.POST.get('count',None)
        slides = Broadcasting.objects.get(pk=1).slides.all()
        try:
            url = slides[int(pos)].file.url
        except:
            url = None
        return HttpResponse(JsonResponse({ 'url': url , 'pos': pos }))
    else:
        return HttpResponse(123)


class SlideViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer
    
class SlideGet(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self,bk, pos):
        #broadcasting = Broadcasting.objects.get(pk=int(bk))
        slides = Broadcasting.objects.get(pk=int(bk)).slides.all()
        try:
            return slides.get(position=pos)
        except Slide.DoesNotExist:
            raise Http404

    def get(self, request, bk, pos, format=None):
        slide = self.get_object(bk,pos)
        serializer = SlideSerializer(slide)
        return Response(serializer.data)
    