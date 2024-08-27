from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path('services/', views.services, name='services'),  
    path('icecream/', views.icecream, name='icecream'),  # Define this
    path('falooda/', views.falooda, name='falooda'),      # Define this
    path('milkshake/', views.milkshake, name='milkshake'),# Define this
    
     
      
    
]
