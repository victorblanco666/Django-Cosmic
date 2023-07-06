from django.shortcuts import render

# Create your views here.


def index(request):
    context= {}
    return render(request,'Guitar/index.html',context)

def login(request):
    context= {}
    return render(request,'Guitar/login.html',context)

def register(request):
    context= {}
    return render(request,'Guitar/register.html',context)

def nivel1(request):
    context={}
    return render(request,'Guitar/nivel-1.html',context)

def nivel2(request):
    context={}
    return render(request,'Guitar/nivel-2.html',context)

def nivel3(request):
    context={}
    return render(request,'Guitar/nivel-3.html',context)


def news(request):
    context={}
    return render(request,'Guitar/news.html')