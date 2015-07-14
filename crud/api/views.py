#from django.contrib.sites import requests
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
import json
from movie.models import Movie
# Create your views here.


# Get request view



def my_get_api(request):
   qs = Movie.objects.all()
   return HttpResponse(serializers.serialize('json', qs), content_type='application/json')



# Post request view




# Delete request view




# Update (put or patch) request view



