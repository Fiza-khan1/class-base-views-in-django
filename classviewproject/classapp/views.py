from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import contactform
from django.views.generic.base import TemplateView,RedirectView
from django.views.generic.list import ListView
from .models import Student
from django.views.generic.detail import DetailView

def home(request):
    return HttpResponse('kbkjdvldrnv')

class MyHomeView(View):  # Use a descriptive and consistent class name
    Name='FIZA'
    def get(self, request):
        return HttpResponse(self.Name)
    

class MyHomeChildView(MyHomeView):  # Use a descriptive and consistent class name
    def get(self, request):
        return HttpResponse(self.Name)
    

class contact(View):
    def get(self,request):
       form=contactform()  
       return render(request,'home.html',{'form':form})
    
    def post(self,request):
       form=contactform(request.POST)
       if form.is_valid():
           return HttpResponse("DONNNNEEEE")
       

class myhometemplate(TemplateView):
    template_name='index.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['name']='Fiza'
        context['roll']='cpen211101015'
        return context


class redirecttopage(RedirectView):
    url='https://www.google.com/search?q=google+url&rlz=1C1ONGR_enPK1087PK1087&oq=google+url&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRhA0gEIMTU3OWowajeoAgCwAgA&sourceid=chrome&ie=UTF-8'

class Redirecttosome(RedirectView):
   pattern_name='mindex'


class display(ListView):
    model=Student
    context_object_name='students'
    def get_queryset(self):
        return Student.objects.filter(course='Django')
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context= super().get_context_data(**kwargs)
        context['new']=Student.objects.all().order_by('id')
        return context

   
class StudentDetailView(DetailView):
    model=Student
    








