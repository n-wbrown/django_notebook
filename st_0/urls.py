from django.conf.urls import url
from st_0 import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$',views.AboutPageView.as_view()),
    url(r'^raw/$',views.raw_response),
    url(r'^list/$',views.box_list),
    url(r'^box([0-9]+)/$',views.single),
    url(r'^bbox(?P<box_id>[0-9]+)/$',views.single)
]
