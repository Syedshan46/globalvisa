from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.

def index(request): 
    return render(request,"app/index.html")

def contact(request):
    if request.method == 'POST':
        name     = request.POST['contact_name']
        email    = request.POST['contact_email']
        subject  = request.POST['contact_subject']
        message  = request.POST['contact_message']
        
        contact = Contact(contact_name=name, contact_email=email, contact_subject=subject, contact_message=message)
        contact.save()
        return redirect('home_page')

