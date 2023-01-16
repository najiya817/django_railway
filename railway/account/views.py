from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def log(request):
    if request.method=="GET":
        return render(request,"login.html")
    elif request.method=="POST":
        #print(request.POST)
        print(request.POST.get("uname"))
        print(request.POST.get("password"))
        return HttpResponse("post request reached")

def register(request):
    if request.method=="GET":
        return render(request,"register.html")
    elif request.method=="POST":
        print(request.POST.get("username"))
        print(request.POST.get("email"))
        return HttpResponse("post request reached")
    