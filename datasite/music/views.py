from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def music(request):
    return render(request, 'music/music.html')

def header(request):
    return render(request, 'music/header.html')

def musicprojects(request):
    return render(request, 'music/musicprojects.html')

def footer(request):
    return render(request, 'music/footer.html')
