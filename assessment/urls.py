from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_view, name='home'),  # Homepage
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
    path('about/', views.about_view, name='about'),
    path('projects/', views.projects_view, name='projects'),
]
