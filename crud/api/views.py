#from django.contrib.sites import requests
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
from movie.models import Movie
# Create your views here.


@csrf_exempt
def my_get_api(request):
   qs = Movie.objects.all()
   return HttpResponse(serializers.serialize('json', qs), content_type='application/json')

@csrf_exempt
def post_api(request, *args, **kwargs):
    movie = Movie.objects.create(title=request.POST['title'])
    movie.save()
    return HttpResponse(status=201)

@csrf_exempt
def delete_api(request, *args, **kwargs):
   movie = Movie.objects.filter(pk=request.POST['pk'])
   movie.delete()
   return HttpResponse(status=200)



# Update (put or patch) request view
@csrf_exempt
def put_api(request):
    first_movie = Movie.objects.filter(pk=request.POST['pk'])
    first_movie.delete()
    new_movie = Movie.objects.create(pk=request.POST['pk'], title=request.POST['title'])
    return HttpResponse(status=200)


