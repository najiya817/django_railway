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
        return render(request,"div.html")
    def post(self,request,*args,**kwargs):
        num1=request.POST.get("n1")
        num2=request.POST.get("n2")
        resl=int(num1)/int(num2)
        return render(request,"div.html",{"data":resl})  
