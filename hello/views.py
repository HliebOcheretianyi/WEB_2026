import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Mea+Culpa&display=swap" rel="stylesheet">

        <h1 style="color: red; font-family: 'Mea Culpa', cursive; font-size: 120px">
            Salam alaikum
        </h1>
    ''')


def fancy_index(request):
    return render(request, "hello/index.html")


def hello_name(request, name):
    data = {
        'name': name.capitalize(),
        'time': datetime.datetime.now(),
        'show_time': True
    }
    return render(request, "hello/greet.html", data)
