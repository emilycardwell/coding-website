from django.shortcuts import render, HttpResponse, redirect
from about.models import Contact
from django.contrib import messages

# Create your views here.
def about(request):
    return render(request, 'about/about.html')

def header(request):
    return render(request, 'about/header.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        title = request.POST['title']
        content = request.POST['content']

        if len(name)<1:
            messages.error(request, "Name is requred")
        elif len(email)<1:
            messages.error(request, "Email is requred")
        elif len(title)<1:
            messages.error(request, "Title is requred")
        elif len(content)<1:
            messages.error(request, "Message is requred")
        elif len(name)<3 or len(email)<5 or len(title)<3 or len(content)<5:
            messages.error(request, "One or more fields are too short")
        else:
            contact = Contact(name=name, email=email, phone=phone, title=title,
                              content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")

    return render(request, 'about/contact.html')

def footer(request):
    return render(request, 'about/footer.html')
