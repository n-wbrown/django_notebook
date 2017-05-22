from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

from django.http import HttpResponse

from .models import box 
from django.db.models import Q



class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class AboutPageView(TemplateView):
#    def get(self, request, **kwargs):
#        return render(request, 'about.html', context=None)
    template_name = "about.html"

def raw_response(request):
    return HttpResponse("<p>This is a raw response page</p><p>end</p>")

def box_list(request):
    box_list = box.objects.filter(mass__gte=2.0)
    context = {'heavy_items':box_list}
    return render(request, 'list.html', context)

