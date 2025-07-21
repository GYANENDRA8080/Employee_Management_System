from django.urls import path, include
from emp_app import views

urlpatterns = [
    
    path('', views.home, name='home'),  # Maps the root URL to the home view
    path('about/', views.about, name='about'),  # Maps the about URL to the about view
]