from django.shortcuts import render

def Inicio(request):
    return render(request,'index.html')