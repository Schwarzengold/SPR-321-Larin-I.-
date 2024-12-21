from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),  
    path('gallery/', views.gallery, name='gallery'), 
]
