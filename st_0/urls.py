from django.conf.urls import url
from st_0 import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$',views.AboutPageView.as_view()),
]