from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='StudentLogin'),
    path('/studentpage',views.studentpage,name="StudentPage"),
    path('/studentPage',views.studentHome,name="StudentHome")

]
