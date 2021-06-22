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
currTeacherLogged = None

def index(request):
    return render(request, 'Teacher/index.html')

def teacherpage(request):
    global name
    global currTeacherLogged
    name = request.POST['username']
    password = request.POST['pass']
    a = Teacher.objects.all()
    flag = False
    for i in a:
        if (i.Teacher_userid == name):
            if (i.Teacher_password == password):
                currTeacherLogged = i
                flag = True
    flag1 = not flag
    params = {'passcheck': flag1}
    if (flag == True):
        return HttpResponseRedirect('teacherhome')
    else:
        return render(request, 'Teacher/index.html', params)

def teacherHome(request):
    if(currTeacherLogged):
        return render(request,'Teacher/TeacherHome.html')
    else:
        return render(request,'Teacher/Loggedout.html')


def Profilepage(request):
    if(currTeacherLogged):

        global name
        d=Teacher.objects.all()
        teacherprofile=[]
        for i in d:

            if(i.Teacher_userid==name):
                teacherprofile=i
                break
        params={'teacher':teacherprofile}
        return render(request, 'Teacher/Profilepage.html',params)
    else:
        return render(request,'Teacher/Loggedout.html')

def QuestionPage(request):
    if(currTeacherLogged):

        a=Questionanswers.objects.all()

        finallst=[]
        print(a)
        for i in a:
                if(i.Answers == ''):
                    finallst.append(i)
        params={'doubts':finallst}
        return render(request,'Teacher/QuestionsPage.html',params)
    else:
        return render(request,'Teacher/Loggedout.html')


def ContactPage(request):
    if(currTeacherLogged):
        return render(request,'Teacher/ContactPage.html')
    else:
        return render(request,'Teacher/Loggedout.html')

def AnsweringPage(request):
    if(currTeacherLogged):
        
        global questioner
        questioner=request.GET.get('questionentry')

        d=Questionanswers.objects.all()
        entry=[]
        for i in d:
            if(i.Question==questioner):
                entry=i
        params={'entry':entry}


        return render(request, 'Teacher/AnsweringPage.html',params)
    else:
        return render(request,'Teacher/Loggedout.html')

def answeredpage(request):
    if(currTeacherLogged):

        global questioner
        answer=request.POST['finalanswer']
        d=Questionanswers.objects.all()
        s=[]
        for i in d:
            if(i.Question==questioner):
                s=i
        s.Answers=answer
        #s.save()
        return render(request, 'Teacher/AnswerSubmitted.html')
    else:
        return render(request,'Teacher/Loggedout.html')

def logout(request):
    global currTeacherLogged
    currTeacherLogged = None
    return render(request,'Teacher/Loggedout.html')
    
