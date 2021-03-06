from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    context={
        "courses": Course.objects.all(),
        "description": Description.objects.all()
    }

    return render(request, "index.html", context)


def submit_course(request):
    errors = Course.objects.validator(request.POST)

    if len(errors)>0:
        for k, v in errors.items():
            messages.error(request, v)

        return redirect('/')

    if len(request.POST['description'])>0:
        new_course=Course.objects.create(
        name=request.POST['name'],
        # description=request.POST['description']
        )
        new_description = Description.objects.create(
        course=new_course, 
        text=request.POST['description'])

    elif len(request.POST['description'])<=0:
        new_course=Course.objects.create(
        name=request.POST['name']
        )
    return redirect('/')

def remove_confirm(request, id):
    context={
        "course": Course.objects.get(id = id)
    }
    return render(request, "remove.html", context)

def remove(request, id):
    remove_course = Course.objects.get(id=id)
    remove_course.delete()
    return redirect("/")

def show_form(request, id):
    context={
        "comments": Comment.objects.filter(course=id),
        "id": id
    }
    return render(request, "comments.html", context)

def comment(request, id):
    new_comment = Comment.objects.create(text=request.POST['comment'], course=Course.objects.get(id=id))
    return redirect (f'/show_form/{id}')


