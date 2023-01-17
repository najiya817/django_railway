from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
# def log(request):
#     if request.method=="GET":
#         return render(request,"login.html")
#     elif request.method=="POST":
#         #print(request.POST)
#         print(request.POST.get("uname"))
#         print(request.POST.get("password"))
#         return HttpResponse("post request reached")

# def register(request):
#     if request.method=="GET":
#         return render(request,"register.html")
#     elif request.method=="POST":
#         print(request.POST.get("username"))
#         print(request.POST.get("email"))
#         return HttpResponse("post request reached")


class LogView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"login.html")
    def post(self,request,*args,**kwargs):
        print(request.POST.get("username"))
        print(request.POST.get("email"))
        return HttpResponse("username:"+request.POST.get("username")+"<br>password:"+request.POST.get("password"))

class RegisterView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"register.html")
    def post(self,request,*args,**kwargs):
        print(request.POST.get("username"))
        print(request.POST.get("password"))
        return HttpResponse("Registred")