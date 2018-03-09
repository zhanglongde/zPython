from django.shortcuts import render,HttpResponse

# Create your views here.

def show_time(req):
    return HttpResponse("hello")