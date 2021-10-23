from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import ContactForm
from django.conf import settings
from django.core.mail import message, send_mail

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name", "")
            content = request.POST.get("content", "")
            email = request.POST.get("email", "")
            link = reverse('contact')
            
            # Se envía un correo
            subject = "Gracias por contactarnos"
            message = "Hola {name} , gracias por ponerse en contacto con nosotros"
            email_from = settings.EMAIL_HOST_USER
            email_for = [email,]

            send_mail(subject, message, email_from,email_for)

            return redirect(link + '?ok') 

    return render(request, 'contact/contact.html', {'form':contact_form})
