from django.shortcuts import render
from django.http import HttpResponse
from core_site_sputnic.settings import BASE_DIR


def index(request):

    print(BASE_DIR)
    return HttpResponse('Hello, World')


