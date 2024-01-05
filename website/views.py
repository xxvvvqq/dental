from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,"index.html",{})

def contact(request):
    if request.method =="POST":
        name = request.POST["name"]
        message = request.POST["message"]
        email = request.POST["email"]
        
        # send an email
        send_mail(
            name, #subject
            message, #message
            email, #email
            
            
            ['bolasamuel.sb@gmail.com'], # email 

             )


        return render(request,"contact.html",{'name': name})

    else:
    
        return render(request,"contact.html",{})

def about(request):
    return render(request,"about.html",{})


def service(request):
    return render(request,"service.html",{})


def departments(request):
    return render(request,"departments.html",{})

def doctors(request):
    return render(request,"doctors.html",{})

def appointment(request):
    return render(request,"appointment.html",{})

