from django.shortcuts import render
from rest_framework import viewsets
from .models import Modulo, User


def index(request):
    return render(request, 'index.html')