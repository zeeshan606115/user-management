from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from student_management_app.models import CustomUser, Staffs, Courses


def admin_home(request):
    return render(request, "hod_template/home_content.html")

def add_staff(request):
    return render(request, "hod_template/add_staff_template.html")

def add_staff_save(request):
    if request.method != 'POST':
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
                user_type = 2
            )
            user.staffs.address=address
            user.save()
            messages.success(request, "Successfully Added Staff")
            return HttpResponseRedirect("/add_staff")
        except:
            messages.error(request, "Something went wrong!!! Try Again")
            return HttpResponseRedirect("/add_staff")


def add_course(request):
    return render(request, "hod_template/add_course_template.html")

def add_course_save(request):
    if request.method != 'POST':
        return HttpResponse("Method Not Allowed")
    else:
        course = request.POST.get('course')
        try:
            course_model= Courses(course_name=course)
            course_model.save()
            messages.success(request, "Successfully Added Course")
            return HttpResponseRedirect("/add_course")
        except:
            messages.error(request, "Something went wrong!!! Try Again")
            return HttpResponseRedirect("/add_course")

def add_student(request):
    return render(request, "hod_template/add_student_template.html")

def add_student_save(request):
    if request.method != 'POST':
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
                user_type = 2
            )
            user.staffs.address=address
            user.save()
            messages.success(request, "Successfully Added Staff")
            return HttpResponseRedirect("/add_student")
        except:
            messages.error(request, "Something went wrong!!! Try Again")
            return HttpResponseRedirect("/add_student")
