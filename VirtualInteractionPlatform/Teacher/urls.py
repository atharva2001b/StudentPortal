from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('/',views.index,name="Teacher Login Page"),
    path('/teacherpage',views.teacherpage,name="Teacherhomepage")
]