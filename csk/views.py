from django.shortcuts import render

# Create your views here.

def dhoni(request):
    return render(request,'dhoni.html')

def ravindra(request):
    return render(request,'ravindra.html')
