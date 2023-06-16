from django.shortcuts import render, redirect
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


# @login_required(login_url="adminapp:login")
def index_view(request):
    context = {'segment': 'index'}
    return render(request, 'home/index.html', context)


# Create your views here.
# @login_required(login_url="adminapp:login")
# def index(request):
#     context = {'segment': 'index'}

#     html_template = loader.get_template('home/index.html')
#     # return HttpResponse(html_template.render(context, request))
#     return render(request, html_template, {})


@login_required(login_url="adminapp:login")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))











def profile_view(request):
    context = {'segment': 'profile'}
    return render(request, 'home/page-user.html', context)


def employee_view(request):
    context = {'segment': 'employee'}
    return render(request, 'home/employee.html', context)


def leave_view(request):
    context = {'segment': 'leave'}
    return render(request, 'home/leave.html', context)


def attendance_view(request):
    context = {'segment': 'attendance'}
    return render(request, 'home/attendance.html', context)



def calender_view(request):
    context = {'segment': 'calender'}
    return render(request, 'home/calender.html', context)



def todo_view(request):
    context = {'segment': 'todo'}
    return render(request, 'home/todo.html', context)