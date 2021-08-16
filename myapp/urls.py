from . import views
from django.urls import path
urlpatterns = [
    path('hello',views.TextFun,name='hello my page'),
    path('index',views.IndexFun,name='index'),
    path('projectdemo',views.ProjectdemoFun,name='projectdemo'),
    path('login',views.LoginFun,name='login'),
    path('demoimage',views.DemoimageFun,name="demoimage"),
]