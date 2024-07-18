from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.MyHomeView.as_view(Name='Muqadas'), name='home'),
    path('cl/', views.MyHomeChildView.as_view(), name='child'),  # Corrected name to 'child'
    path('contact/', views.contact.as_view(), name='contact'),  # Corrected class name to 'Contact'
    path('some/', TemplateView.as_view(template_name='home.html'), name='index'),  # Assuming 'myhometemplate' was supposed to use TemplateView
    path('redi/', RedirectView.as_view(url='/cl/'), name='redi'),
    path('info/',views.redirecttopage.as_view(),name='info'),
    path('something/',views.RedirectView.as_view(pattern_name='info'),name='something'),
    path('info/<int:pk>/',views.Redirecttosome.as_view(),name='infointe'),
    path('<int:pk>/',views.TemplateView.as_view(template_name='home.html'),name='mindex'),
    path('display/',views.display.as_view(),name='display'),
    path('displaymodel/<int:pk>/', views.StudentDetailView.as_view(), name='displaymodel'),

    
]
