from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def header(request):
    return render(request, 'home/header.html')

def blurb(request):
    return render(request, 'home/blurb.html')

def projects(request):
    return render(request, 'home/projects.html')

def footer(request):
    return render(request, 'home/footer.html')
