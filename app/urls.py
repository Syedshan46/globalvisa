from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name="home_page"),
    path('contact', views.contact, name="contact")
]
