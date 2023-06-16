from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse

# Create your views here.

def login_view(request):
    print("=================== Login View")
    if request.method == 'POST':
        print("Form Data :: ", request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        print("User ========", user.is_staff)

        if user is not None:
            login(request, user)
            return redirect(reverse('webapp:index'))
    return render(request, 'accounts/login.html', {})

def logout_view(request):
    logout(request)
    return HttpResponsePermanentRedirect(reverse_lazy('adminapp:login'))

def forget_password_view(request):
    return HttpResponse("Password Reset Page")