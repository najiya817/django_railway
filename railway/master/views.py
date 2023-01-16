from django.shortcuts import render

# Create your views here.
def home(request):
    name="NASRIN"
    lst=["apple","orange","mango"]
    return render(request,"home.html",{"data":name,"list":lst})