from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','status')
    list_filter = ('status','name',)