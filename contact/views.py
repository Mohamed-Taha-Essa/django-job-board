from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def send_message(request):
   info = Info.objects.first()

   
   if request.method == 'POST':
      email = request.POST['email']
      subject =request.POST['subject']
      message = request.POST['message']
      # print(subject)
      # print(email)
      send_mail(
            subject,
           message,
            settings.EMAIL_HOST_USER,
            [email],
               )


   return render(request ,'contact/contact.html' ,{'info':info})
