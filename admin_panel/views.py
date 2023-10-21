from django.shortcuts import render,redirect
from .models import Register
from app.models import Contact

# Create your views here.
def register(request):
    if request.method == 'POST':
        reg_name = request.POST['reg_name']
        reg_pass = request.POST['reg_pass']
        
        register = Register(reg_name=reg_name,reg_pass=reg_pass)
        register.save()
        
    return render(request,"admin/register.html")

def adminlogin(request):
    if 'userses' in request.session:
        return redirect(dashboard)
    if request.method == 'POST':
        log_user = request.POST['log_user']
        log_pass = request.POST['log_pass']
        
        login = Register.objects.filter(reg_name=log_user, reg_pass=log_pass)
        if login:
            request.session['userses'] = log_user
            return redirect('dashboard')
    return render(request,"admin/adminlogin.html")

def dashboard(request): 
    contact = Contact.objects.all()
    context = {
        "contact": contact
    }
    return render(request,"admin/dashboard.html", context)

