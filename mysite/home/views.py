from django.shortcuts import render

from django.contrib import messages


# Create your views here.
from .models import Contact
def home(request):
    return render(request, 'home/index.html')

def contact(request):
    if request.method =="POST":
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        msg= request.POST['msg']
        if len(name)<2 or len(email)<10 or len(phone)<10 or len(msg)<2:
            messages.error(request,"You have somthing wrong please Try again. !!!!!")
        elif len(phone)>10 :
            messages.error(request,"You have somthing wrong please Try again. !!!!!")

        else:
            contact= Contact(name=name, email=email, phone=phone, msg=msg )
            contact.save()

            messages.success(request,"Your data is successfully sended.!!!")
    return render(request, 'home/contact.html')

def privacy(request):
    return render(request, 'home/privacy.html')

def tnc(request):
    return render(request, 'home/tnc.html')


def about(request):
    return render(request, 'home/about.html')

    
def search (request):
    return render(request, 'home/search.html')