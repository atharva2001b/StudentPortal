from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='StudentLogin'),
    path('/StudentLoginPage',views.studentLoginPage,name="StudentPage"),
    path('/studentPage',views.studentHome,name="StudentHome"),
    path('/studentPage/profilepage',views.profilepage,name="profilepage"),
    path('/studentPage/doubtspage',views.doubtspage,name="doubtpage"),
    path('/studentPage/doubtSubmitted',views.doubtSubmit,name="doubtSubmited"),
    path('/studentPage/contactsPage',views.contacts,name="contacts"),
    path('/studentPage/showanswerspage',views.show,name="showans")
]
