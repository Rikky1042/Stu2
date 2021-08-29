from django.contrib import admin
from .models import Student

@admin.register(Student)
# Register your models here.
class Studentadmin(admin.ModelAdmin):
   list_display= ['id','name','roll','marks']
