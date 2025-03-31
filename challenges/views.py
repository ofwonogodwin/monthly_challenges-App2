from django.shortcuts import render
# Create your views here.

def jan(request):
    return render(request,'jan.html')

def feb(request):
    return render(request,'feb.html')

def mar(request):
    return render(request,'mar.html')

def apr(request):
    return render(request,'apr.html')

def may(request):
    return render(request,'may.html')

def jun(request):
    return render(request,'jun.html')

def jul(request):
    return render(request,'jul.html')

def aug(request):
    return render(request,'aug.html')

def sep(request):
    return render(request,'sep.html')

def oct(request):
    return render(request,'oct.html')

def nov(request):
    return render(request,'nov.html')

def dec(request):
    return render(request,'dec.html')
