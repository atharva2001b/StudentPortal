
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import  HttpResponse
from .models import Students,Questionanswers
# Create your views here.

name = ""

currStudentLogged = None

def index(request):
    return render(request,'Student/StudentLoginPage.html')

def studentLoginPage(request):
    global name
    global currStudentLogged
    name=request.POST['username']
    password=request.POST['pass']
    a=Students.objects.all()
    flag=False
    for i in a:
        if(i.username==name and i.password==password):
            currStudentLogged = i
            flag = True
            
    flag1= not flag
    params={'passcheck':flag1, 'currStudentLogged': currStudentLogged}
    if(flag==True):
        return HttpResponseRedirect('studentPage')
    else:
        return render(request,'Student/StudentLoginPage.html', params)


def studentHome(request):
    if(currStudentLogged):
        d=Students.objects.all()
        studentprofile=[]
        for i in d:
            if(i.username==name):
                studentprofile=i
        params={'student':studentprofile}
        return render(request, 'Student/studentPage.html', params)
    else:
        return render(request,'Student/StudentLoginPage.html')

def profilepage(request):
    if(currStudentLogged):
        d=Students.objects.all()
        studentprofile = []
        for i in d:
            if (i.username == name):
                studentprofile = i
        print(studentprofile)
        params = {'student': studentprofile}
        return render(request,'Student/profilepage.html', params)
    else:
        return render(request,'Student/StudentLoginPage.html')

def doubtspage(request):
    if(currStudentLogged):
        question=request.GET.get('doubt','')
        d = Students.objects.all()
        rno=0

        for i in d:
            if (i.username == name):
                studentprofile = i
                rno=i.rollnumber
        if not (question==""):
            q=Questionanswers(Question=question,rollnumber=rno)
            q.save()
        return render(request,'Student/doubtspage.html', {'student': studentprofile})
    else:
        return render(request,'Student/StudentLoginPage.html')


def doubtSubmit(request):
    if(currStudentLogged):
        question=request.GET.get('doubt','')
    if not (question==""):
            q=Questionanswers(Question=question, rollnumber = currStudentLogged.rollnumber)
            q.save()

    return render(request,'Student/doubtSubmitted.html', None)

def contacts(request):
    if(currStudentLogged):
        return render(request,'Student/contactsPage.html', None)
    else:
        return render(request,'Student/StudentLoginPage.html')


