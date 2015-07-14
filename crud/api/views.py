#from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.


# Get request view
import requests


def my_get_api(request):
    response = requests.get('movie:movie_list')


   # response.content
   # variable = json.
    return HttpResponse(response)



# Post request view




# Delete request view




# Update (put or patch) request view



