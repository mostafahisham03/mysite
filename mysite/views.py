from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse('Here is the home page.')
    return render(request, 'home.html', {'greeting': 'Hello!'})


def about(request):
    # return HttpResponse('Here is the about page.')
    return render(request, 'about.html')
