from django.shortcuts import render
from django.views.generic  import View
from .forms import AddForm

# Create your views here.
class AddView(View):
    def get(self,request,*args,**kwargs):
        f=AddForm
        return render(request,"add.html",{"form":f})
    def post(self,request,*args,**kwargs):
        num1=request.POST.get("num1")
        num2=request.POST.get("num2")
        res=int(num1)+int(num2)
        return render(request,"add.html",{"data":res})


class SubView(View):
    def get(self,request,*args,**kwargs):
        f=AddForm
        return render(request,"sub.html",{"form":f})
    def post(self,request,*args,**kwargs):
        num1=request.POST.get("num1")
        num2=request.POST.get("num2")
        resl=int(num1)-int(num2)
        return render(request,"sub.html",{"data":resl})

class MulView(View):
    def get(self,request,*args,**kwargs):
        f=AddForm
        return render(request,"mul.html",{"form":f})
    def post(self,request,*args,**kwargs):
        num1=request.POST.get("num1")
        num2=request.POST.get("num2")
        resl=int(num1)*int(num2)
        return render(request,"mul.html",{"data":resl})  


class CountView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"wrdcnt.html")
    def post(self,request,*args,**kwargs):
        sent=request.POST.get("strng")
        words=sent.split(" ")
        cnt={}
        for i in words:
            if i in cnt:
                cnt[i]+=1
            else:
                cnt[i]=1
        return render(request,"wrdcnt.html",{"res":cnt})
    
class DivView(View):
    def get(self,request,*args,**kwargs):
        f=AddForm
        return render(request,"div.html",{"form":f})
    def post(self,request,*args,**kwargs):
        num1=request.POST.get("num1")
        num2=request.POST.get("num2")
        resl=int(num1)/int(num2)
        return render(request,"div.html",{"data":resl})  
