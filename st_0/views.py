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
    return HttpResponse("<p>This is a raw response page</p>"+
                        '<a href="/st/">Return home</a>'+
                        "<p>end</p>")
def box_list(request):
    #box_list = box.objects.filter(mass__gte=2.0)
    box_list = box.objects.all()
    context = {'heavy_items':box_list}
    return render(request, 'list.html', context)

def single(request,*args,**kwargs):
    print("args: ",args)
    print("kwargs: ",kwargs)
    if (args):
        target = box.objects.filter(pk=int(args[0]))
    elif (kwargs):
        target = box.objects.filter(pk=int(kwargs['box_id']))
    else:
        target = []
    print(target[0].mass)
    context = {'args':args,'kwargs':kwargs,'target':target}
    #selected_box = box.objects.flter(pk=
    return render(request,"single.html",context)
