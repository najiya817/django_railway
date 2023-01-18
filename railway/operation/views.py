from django.shortcuts import render
from django.views.generic  import View

# Create your views here.
class AddView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"add.html")
    def post(self,request,*args,**kwargs):
        num1=request.POST.get("n1")
        num2=request.POST.get("n2")
        res=int(num1)+int(num2)
        return render(request,"add.html",{"data":res})


class SubView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"sub.html")
    def post(self,request,*args,**kwargs):
        num1=request.POST.get("n1")
        num2=request.POST.get("n2")
        resl=int(num1)-int(num2)
        return render(request,"sub.html",{"data":resl})

class MulView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"mul.html")
    def post(self,request,*args,**kwargs):
        num1=request.POST.get("n1")
        num2=request.POST.get("n2")
        resl=int(num1)*int(num2)
        return render(request,"mul.html",{"data":resl})        