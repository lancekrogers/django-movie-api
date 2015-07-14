from django.conf.urls import include, url

from .views import MovieListView, MovieCreateView, MovieDeleteView, MovieDetailView


urlpatterns = [

    url(r'^movie_list/$', MovieListView.as_view(), name="movie_list"),
    url(r'^create_movie/$', MovieCreateView.as_view(), name="create_movie"),
    url(r'^delete_movie/(?P<pk>\d+)/$',MovieDeleteView.as_view(), name="delete_movie"),
    url(r'^movie_detail/(?P<pk>\d+)/$',MovieDetailView.as_view(), name="movie_detail"),

    ]