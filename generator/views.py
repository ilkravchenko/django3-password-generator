from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    chars = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('Uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Special'):
        chars.extend(list('!@#$%^&*()_-'))
    if request.GET.get('Numbers'):
        chars.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))

    the_password = ''
    for x in range(length):
        the_password += random.choice(chars)

    return render(request, 'generator/password.html',{'password':the_password})

def about(request):
    return render(request, 'generator/about.html')