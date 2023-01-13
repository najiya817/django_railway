from django.shortcuts import render

# Create your views here.
def home(request):
    name="NASRIN"
    return render(request,"home.html",{"data":name})