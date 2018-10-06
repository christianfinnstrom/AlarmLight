from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    return render(request, 'AlarmInput/index.html')


def setAlarm(request):
    return render(request, 'AlarmInput/setAlarm.html')