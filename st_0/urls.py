from django.conf.urls import url
from st_0 import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$',views.AboutPageView.as_view()),
    url(r'^raw/$',views.raw_response),
    url(r'^list/$',views.box_list),
]
