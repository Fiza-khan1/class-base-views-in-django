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
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from .forms import contactform,StudentForm
from django.urls import reverse_lazy
from django import forms
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
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context= super().get_context_data(**kwargs)
        context['new']=Student.objects.all()
        return context
    
    

class ViewContactForm(FormView):
    template_name='classapp/formview.html'
    form_class=contactform  
    def form_valid(self, form: Any) -> HttpResponse:
        print(form)
        return super().form_valid(form)
    
# class studentCreateForm(CreateView):
#     model=Student
#     fields=['name','age','course']

#     def get_form(self):
#         form= super().get_form()
#         form.fields['name'].widget.attrs.update({'class': 'custom-class', 'placeholder': 'Enter name'})
#         form.fields['age'].widget.attrs.update({'class': 'custom-class', 'placeholder': 'Enter age'})
#         form.fields['course'].widget.attrs.update({'class': 'custom-class', 'placeholder': 'Enter course'})
#         return form
    # success_url = reverse_lazy('end')

class studentCreateForm(CreateView):
    form_class=StudentForm
    template_name='classapp/student_form.html'

    
class studentupdateview(UpdateView):
    model = Student
    fields = ['name', 'age', 'course']
    success_url = reverse_lazy('update_success') 

class studentdeleteview(DeleteView):
    model=Student
    success_url = '/home/'

    
class TemplateEndView(TemplateView):
    template_name = 'msg.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = self.kwargs['id']
        context['student'] = Student.objects.get(id=self.kwargs['id'])    
        return context
        

class msgtemplate(TemplateView):
    template_name = 'msg.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg'] = 'Object deleted '
        return context
        
class update(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("UPDATED SUCCESSFULLY")






