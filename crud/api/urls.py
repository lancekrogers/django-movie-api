from django.conf.urls import include, url
from .views import my_get_api

urlpatterns = [

    url(r'^movie_list/', my_get_api, name='get_api')

]