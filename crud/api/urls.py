from django.conf.urls import include, url
from .views import my_get_api, post_api, delete_api, put_api

urlpatterns = [

    url(r'^get/', my_get_api, name='get_api'),
    url(r'^post/', post_api),
    url(r'^delete/', delete_api),
    url(r'^put/', put_api)


]