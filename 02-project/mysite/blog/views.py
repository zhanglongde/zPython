from django.shortcuts import render,HttpResponse
import time
# Create your views here.

def show_time(req):
    # return HttpResponse("hello")
    t=time.ctime()
    return render(req,"index.html", {"time": t})