from django.contrib import admin
from .models import Student

@admin.register(Student)
class studentadmin(admin.ModelAdmin):
    list_display=['id','name','age','course']
# Register your models here.
