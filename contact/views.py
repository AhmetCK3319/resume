from django.shortcuts import render
from django.http import JsonResponse
from .models import Message
from .forms import ContactForm


def contact_form(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST or None)
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            Message.objects.create(name=name,
                                   email=email,
                                   subject=subject,
                                   message=message
                                   )
            contact_form.send_mail()
            success = True
            message = "Thank you for your message. We will get back to you soon."
        else:
            success = False
            message = "Contact form is not valid"
    else:
        success = False
        message = "Sorry, we are unable to contact you. Please try again."
    context = {
        'success': success,
        'messages': message,
    }
    return JsonResponse(context)


def contact(request):# contact_form gönderilmesinin sebebi validasyonları html uygulamak için
    contact_form = ContactForm()
    context = {
        'contact_form': contact_form,
    }
    return render(request, 'contact.html',context)
