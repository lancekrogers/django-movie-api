from django.core.urlresolvers import reverse
from django.http import HttpResponse
from movie.models import Movie
from django.shortcuts import render
from rest_framework import generics, serializers
# Create your views here.


class MySerializer(serializers.ModelSerializer):
    ser = serializers.SerializerMethodField()

    def get_ser(self, obj):
        return reverse('rest_api:hello', kwargs={'pk': obj.pk})

    class Meta:
        model = Movie
        fields = ['ser', 'title']


class MovieViewApi(generics.ListAPIView):
    serializer_class = MySerializer
    queryset = Movie.objects.all()


class CreateMovie(generics.CreateAPIView):
    serializer_class = MySerializer
    queryset = Movie.objects.all()


class GetPostMovie(generics.RetrieveAPIView):
    serializer_class = MySerializer
    queryset = Movie.objects.all()


class UpdateDeleteAndRetrieve(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MySerializer
    queryset = Movie.objects.all()

