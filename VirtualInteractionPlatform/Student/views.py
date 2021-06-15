from django.db.models.fields import NullBooleanField
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import  HttpResponse
from .models import Students
# Create your views here.

def index(request):
    return render(request,'Student/StudentLoginPage.html')

def studentpage(request):
    name=request.POST['username']
    password=request.POST['pass']
    print(name)
    print(password)
    a=Students.objects.all()
    print(a[0].username)
    print((a[0].password))
    flag=False
    for i in a:
        if(i.username==name and i.password==password):
            flag=True
    flag1= not flag
    params={'passcheck':flag1}
    if(flag==True):
        return HttpResponseRedirect('studentPage')
    else:
        return render(request,'Student/StudentLoginPage',params)


def studentHome(request):
    return render(request, 'Student/studentPage.html')


