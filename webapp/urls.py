from django.urls import path, re_path

from . import views

app_name = 'webapp'

urlpatterns = [
    # TODO: webapp urls
    path('', views.index_view, name='index'),
    path('profile/', views.profile_view, name='profile'),
    path('employee/', views.employee_view, name='employee'),
    path('leave/', views.leave_view, name='leave'),
    path('attendance/', views.attendance_view, name='attendance'),
    path('calender/', views.calender_view, name='calender'),
    path('todo/', views.todo_view, name='todo'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
]