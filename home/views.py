from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    text = "<h1>home<h1>"
    return HttpResponse(text)
def login(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request,'login.html',context)
def register(request):
    text = "<h1>register<h1>"
    return HttpResponse(text)
def security(request):
    text = "<h1>Security<h1>"
    return HttpResponse(text)
def visitor(request):
    text = "<h1>visitor<h1>"
    return HttpResponse(text)