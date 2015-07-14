from django.conf.urls import include, url
from rest_api.views import MovieViewApi, CreateMovie, GetPostMovie, UpdateDeleteAndRetrieve

urlpatterns = [

    url(r'^movie_list/$', MovieViewApi.as_view(), name='api_movie'),
    url(r'^movie_list/(?P<pk>\d+)/detail/$', GetPostMovie.as_view()),
    url(r'^movie_list/create/$', CreateMovie.as_view()),
    url(r'^movie_list/(?P<pk>\d+)/$', UpdateDeleteAndRetrieve.as_view(), name='hello'),

]