# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response, redirect 
from django.template import RequestContext
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from broadcasts.models import Broadcasting, Slide
from broadcasts.serializers import SlideSerializer
from rest_framework import viewsets

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