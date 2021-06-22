from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('/',views.index,name="teacherlogin"),
    path('/teacherpage',views.teacherpage,name="Teacherloginpage"),
    path('/teacherhome',views.teacherHome,name="TeacherHomepage"),
    path('/teacherhome/profilepage',views.Profilepage,name="ProfilePage"),
    path('/teacherhome/questionpage',views.QuestionPage,name="QuestionPage"),
    path('/teacherhome/ContactPage',views.ContactPage,name="ContactPage"),
    path('/teacherhome/questionpage/AnsweringPage',views.AnsweringPage,name="AnsweringPage"),
    path('/teacherhome/questionpage/AnsweringPage/answeredpage',views.answeredpage, name="AnsweredPage"),
    path('/teacherhome/logout',views.logout, name="teacherlogout")
]