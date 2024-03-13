from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def homePageView(request):
    time = datetime.now().strftime('%Y/%m/%d %H: %M: %S')
    return HttpResponse("Testing, hello! The current time is: " + time)