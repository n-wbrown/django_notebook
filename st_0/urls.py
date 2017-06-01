from django.conf.urls import url
from st_0 import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(),name='home'),
    url(r'^about/$',views.AboutPageView.as_view(),name='about'),
    url(r'^raw/$',views.raw_response,name='raw'),
    url(r'^list/$',views.box_list,name='list'),
    url(r'^box([0-9]+)/$',views.single,name='args'),
    url(r'^bbox(?P<box_id>[0-9]+)/$',views.single,name='kwargs'),
    url(r'^detailview(?P<pk>\d+)/$',views.boxDetailView.as_view(),name='class'),
    url(r'^listview(?P<pke>\d+)/$',views.boxListView.as_view(),name='list_view'),
    
]
