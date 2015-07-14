from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.


# Get request view
def my_get_api(request):
    response = request.GET('movie:movie_list')


   # response.content
   # variable = json.
    return HttpResponse('hello')



# Post request view




# Delete request view




# Update (put or patch) request view



