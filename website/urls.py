from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.index, name="index"),
    path('contact.html' ,views.contact, name="contact"),
    path('index.html' ,views.index, name="index"),
    path('about.html' ,views.about, name="about"),
    path('service.html' ,views.service, name="service"),
    path('departments.html' ,views.departments, name="department"),
    path('doctors.html' ,views.doctors, name="doctors"),
    path('appointment.html' ,views.appointment, name="appointment"),
]
