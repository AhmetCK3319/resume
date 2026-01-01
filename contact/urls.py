from django.urls import path
from .views import contact

urlpatterns = [
    path("contact", contact, name="contact"),
    path("contact_form", contact, name="contact_form"),
]