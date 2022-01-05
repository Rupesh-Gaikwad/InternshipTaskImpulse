from django.contrib import admin
from taskApp.models import StudentTask
# Register your models here.

class StudentTaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','description', 'email', 'createdAt']

admin.site.register(StudentTask, StudentTaskAdmin)