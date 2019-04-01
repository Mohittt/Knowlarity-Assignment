from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^showdata$', views.showdata, name='showdata'),
    url(r'^$', views.getdata, name='getdata'),
]