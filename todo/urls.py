
from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('create',create_task),
    path('about-us',about_us),  
    path('task/<pk>/edit',edit),
    path('task/<pk>/mark',mark),
    path('task/<pk>/delete',delete),
    # path('task/add',add),
    
      
]
