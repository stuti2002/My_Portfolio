from django.http.response import HttpResponse
from django.shortcuts import render

from home.models import Contacts

# Create your views here.
def index(request):
    if request.method=='POST':
        name=request.POST.get('Name')
        email=request.POST.get('Email')
        subject=request.POST.get('Subject')
        message=request.POST.get('Message')
        contact= Contacts(Name=name,Email=email,Subject=subject,Message=message)
        contact.save()
    return render(request, 'index.html')
