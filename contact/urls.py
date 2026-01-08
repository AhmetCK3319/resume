from django.urls import path
from .views import contact,contact_form

urlpatterns = [
    path("contact", contact, name="contact"),
    path("contact_form", contact_form, name="contact_form"),
]