from django.shortcuts import render
from django.http import JsonResponse


def contact(request):
    return render(request, 'contact.html')

def contact_form(request):
    context = {'success': True,'message':'Contact Form Message sent successfully'}
    return JsonResponse(context)