from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import View,CreateView,ListView,UpdateView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


from myapp.forms import SignUpForm,SignInForm,MobilePhoneForm
from myapp.models import MobileStore

# Create your views here.
class SignUpView(CreateView):
    model=User
    template_name="signup.html"
    form_class=SignUpForm
    success_url=reverse_lazy("signin")

class SignInView(View):
    model=User
    template_name="signin.html"
    form_class=SignInForm

    def get(self,request,*args,**kwargs):
        form=self.form_class
        return render(request,self.template_name,{"form":form})
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login succeessfull")
                return redirect("mobiles")
        messages.error(request,"login failed")
        return render(request,self.template_name,{"form":form})
    
class MobileListView(ListView):
    model=MobileStore
    template_name="mobilelist.html"
    context_object_name="mobiles"

class MobileCreateView(CreateView):
    model=MobileStore
    template_name="mobileCreate.html"
    form_class=MobilePhoneForm
    success_url=reverse_lazy("mobiles")
    
class MobileDetailView(DetailView):
    model=MobileStore
    template_name="mobileDetail.html"
    context_object_name="mobile"

class MobileUpdateView(UpdateView):
    model=MobileStore
    template_name="mobileUpdate.html"
    form_class=MobilePhoneForm
    success_url=reverse_lazy("mobiles")
    
class MobileDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=MobileStore.objects.get(id=id).delete()
        return redirect("mobiles")
