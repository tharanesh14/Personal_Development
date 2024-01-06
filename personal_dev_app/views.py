from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def year(request):
    return render(request,'year.html')