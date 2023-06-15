from django.urls import path

from . import views

app_name = 'adminapp'

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('forget-password', views.forget_password_view, name="forget-password"),
]