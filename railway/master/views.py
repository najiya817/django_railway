from django.shortcuts import render
from django.views.generic import View

# Create your views here.
# def home(request):
#     name="NASRIN"
#     lst=["apple","orange","mango"]
#     return render(request,"home.html",{"data":name,"list":lst})


class HomeView(View):
    def get(self,request,*args,**kwargs):
        name="NASRIN"
        lst=["apple","orange","mango"]
        exp=0
        return render(request,"home.html",{"data":name,"list":lst,"cndn":exp})
