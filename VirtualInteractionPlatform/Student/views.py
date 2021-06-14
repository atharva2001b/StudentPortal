from django.shortcuts import render
from django.http import  HttpResponse
from .models import Students
# Create your views here.

def index(request):
    return render(request,'Student/StudentLoginPage.html')

def studentpage(request):
    name=request.GET.get('username','default')
    password=request.GET.get('pass','default')
    print(name)
    print(password)
    a=Students.objects.all()
    print(a[0].username)
    print((a[0].password))
    flag=False
    for i in a:
        if(i.username==name):
            if(i.password==password):
                flag=True
    flag1= not flag
    params={'passcheck':flag1}
    if(flag==True):
        return HttpResponse("hii")
    else:
        return render(request,'Student/StudentLoginPage.html',params)


