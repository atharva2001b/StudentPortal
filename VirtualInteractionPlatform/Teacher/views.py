from django.shortcuts import render
from  django.http import HttpResponse
from .models import Teacher
# Create your views here.

def index(request):
    return render(request, 'Teacher/index.html')

def teacherpage(request):
    name = request.GET.get('username', 'default')
    password = request.GET.get('pass', 'default')
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
        return HttpResponse("hii")
    else:
        return render(request, 'Teacher/index.html', params)
