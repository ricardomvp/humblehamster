from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse


def home(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'base/index.html')
