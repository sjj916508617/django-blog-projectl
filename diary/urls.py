
from django.conf.urls import url

from . import views

app_name = 'diary'
urlpatterns = [
    url(r'^diary/$', views.get_diary, name='get_diary'),
]