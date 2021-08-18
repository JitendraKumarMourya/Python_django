from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def TextFun(request):
    return HttpResponse('this my views page')
def IndexFun(request):
    return render(request,'index.html')
def LoginFun(request):
    return render(request,'login.html')
def DemoimageFun(request):
    return render(request,'demoimage.html')
def ProjectFun(request):
    return render(request,'project_demo.html')