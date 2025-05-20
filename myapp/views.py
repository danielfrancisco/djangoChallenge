from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests

def get_data(request):
   return JsonResponse({'data':'hello world!'})
    
