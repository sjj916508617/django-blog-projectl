
from django.conf.urls import url

from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^guestbook/$', views.get_form, name='get_form'),

]