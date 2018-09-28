from django.shortcuts import render

from django.http import HttpResponse



def home(request):

    return render(request, 'home.html', {"html_variable": 'Testing variable operation'})


def home2(request):

    return render(request, 'home2.html', {"html_variable": 'Testing variable operation'})


def home3(request):

    return render(request, 'home3.html', {"html_variable": 'Testing variable operation'})
