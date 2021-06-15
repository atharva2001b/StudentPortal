from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='StudentLogin'),
    path('/StudentLoginPage',views.studentLoginPage,name="StudentPage"),
    path('/studentPage',views.studentHome,name="StudentHome"),
    path('/studentPage/profilepage',views.profilepage,name="profilepage"),
    path('/studentPage/doubts',views.doubtspage,name="doubtpage")
]
