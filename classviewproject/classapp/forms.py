from django import forms
from .models import Student

class contactform(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    course=forms.CharField(max_length=50)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'course']


    