from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from  django.http import HttpResponse
from .models import Teacher
import sys
sys.path.append('E:\VirtualInteractionPlatformactual2\VirtualInteractionPlatform/Student')
from Student.models import Questionanswers
# Create your views here.
name=""
questioner=""

def index(request):
    return render(request, 'Teacher/index.html')

def teacherpage(request):
    global name
    name = request.POST['username']
    password = request.POST['pass']
    print(name)
    print(password)
    a = Teacher.objects.all()
    print(a[0].Teacher_userid)
    print((a[0].Teacher_password))
    flag = False
    for i in a:
        if (i.Teacher_userid == name):
            if (i.Teacher_password == password):
                flag = True
    flag1 = not flag
    params = {'passcheck': flag1}
    if (flag == True):
        return HttpResponseRedirect('teacherhome')
    else:
        return render(request, 'Teacher/index.html', params)

def teacherHome(request):
    return render(request,'Teacher/TeacherHome.html')

def Profilepage(request):
    global name
    d=Teacher.objects.all()
    teacherprofile=[]
    for i in d:

        if(i.Teacher_userid==name):
            teacherprofile=i
            break
    params={'teacher':teacherprofile}
    return render(request, 'Teacher/Profilepage.html',params)

def QuestionPage(request):
    a=Questionanswers.objects.all()

    finallst=[]
    print(a)
    for i in a:
            if(i.Answers == ''):
                finallst.append(i)
    params={'doubts':finallst}
    return render(request,'Teacher/QuestionsPage.html',params)

def ContactPage(request):
    return render(request,'Teacher/ContactPage.html')

def AnsweringPage(request):
    global questioner
    questioner=request.GET.get('questionentry')

    d=Questionanswers.objects.all()
    entry=[]
    for i in d:
        if(i.Question==questioner):
            entry=i
    params={'entry':entry}


    return render(request, 'Teacher/AnsweringPage.html',params)

def answeredpage(request):
    global questioner
    answer=request.GET.get('finalanswer')
    d=Questionanswers.objects.all()
    s=[]
    for i in d:
        if(i.Question==questioner):
            s=i
    s.Answers=answer
    s.save()
    return HttpResponse("Hi")



