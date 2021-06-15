
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import  HttpResponse
from .models import Students
# Create your views here.

name = ""
def index(request):
    return render(request,'Student/StudentLoginPage.html')

def studentLoginPage(request):
    global name
    name=request.POST['username']
    password=request.POST['pass']
    a=Students.objects.all()
    flag=False
    for i in a:
        if(i.username==name and i.password==password):
            flag = True
            
    flag1= not flag
    params={'passcheck':flag1}
    if(flag==True):
        return HttpResponseRedirect('studentPage')
    else:
        return render(request,'Student/StudentLoginPage.html', params)


def studentHome(request):
    d=Students.objects.all()
    studentprofile=[]
    for i in d:
        if(i.username==name):
            studentprofile=i
    params={'student':studentprofile}
    return render(request, 'Student/studentPage.html', params)

def profilepage(request):
    d=Students.objects.all()
    studentprofile = []
    for i in d:
        if (i.username == name):
            studentprofile = i
    print(studentprofile)
    params = {'student': studentprofile}
    return render(request,'Student/profilepage.html',params)

def doubtspage(request):
    return render(request,'Student/doubtspage.html')
