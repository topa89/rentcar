from django.shortcuts import render
from django.http import JsonResponse

from .models import Subscribers

def sub_adding(request):
    return_dict = dict()
    data = request.POST
    email = data.get('email')
   
    new_sub = Subscribers.objects.create(email=email) 
    return JsonResponse(return_dict)