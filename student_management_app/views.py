from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from student_management_app.EmailBackEnd import EmailBackEnd


def showDemo(request):
    return render(request, 'demo.html')

def showLogin(request):
    return render(request, 'login.html')

def dologin(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Method Not Allowed</h2>')
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user != None:
            login(request, user)
            return HttpResponseRedirect("/admin_home")
        else:
            messages.error(request, "Invalid login credentials")
            return HttpResponseRedirect("/")

def get_user_detail(request):
    if request.user != None:
        return HttpResponse("User: "+ request.user.email+ " usertype: "+ request.user.user_type)
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
