from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def profile(request):
    return HttpResponse("I m in student Profile")