from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Я обещаю выучить html и разобраться в программировании!")

