from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

from .models import box 
from django.db.models import Q

from django.views import generic

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from .forms import configureBox

from django.core.urlresolvers import reverse

from django.shortcuts import get_object_or_404

 
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context={'user':request.user,})

class AboutPageView(TemplateView):
#    def get(self request, **kwargs):
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

#@login_required(login_url="accounts/login/")
@method_decorator(login_required,name='dispatch')
class boxDetailView(generic.DetailView):
    model = box
    template_name = 'box_detail.html'

#@login_required(login_url="accounts/login/")
@method_decorator(login_required,name='dispatch')
class boxListView(generic.ListView):
    model = box
    template_name = 'box_list_view.html'
    context_object_name = 'box'
    paginate_by=20

    def get_queryset(self):
        #filter_val = self.request.GET.get('filter', 'give-default-value')
        #order = self.request.GET.get('orderby', 'give-default-value')
        new_context = box.objects.all().order_by('box_name')
        return new_context

def add_box(request):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = configureBox(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            #book_inst.due_back = form.cleaned_data['renewal_date']
            #book_inst.save()
            new_box = box()
            new_box.mass = form.cleaned_data['new_mass']
            new_box.box_name = form.cleaned_data['new_name']
            new_box.colors = form.cleaned_data['new_color']
            new_box.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('list_view'))

    else:
        #proposed_mass = form.new_mass * -1
        #form = configureBox(initial={'new_mass': proposed_mass,})
        form = configureBox()

    return render(request, 'addbox.html', {'form': form,})
 


def mod_box(request,pk):
    box_inst=get_object_or_404(box, pk = pk)
    
    if request.method == 'POST':
        form = configureBox(request.POST)
       
        if form.is_valid():
            box_inst.mass = form.cleaned_data['new_mass']
            box_inst.box_name = form.cleaned_data['new_name']
            box_inst.colors = form.cleaned_data['new_color']
            box_inst.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('list_view'))

    else:
        fill_in = {
            'new_mass':box_inst.mass,
            'new_name':box_inst.box_name,
            'new_color':box_inst.colors,
        }
        form=configureBox(initial = fill_in)


    return render(request, 'addbox.html', {'form': form,})
