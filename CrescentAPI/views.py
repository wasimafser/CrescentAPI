from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth

# def login_view(request):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     user = auth.authenticate(username=username, password=password)
#     if user is not None and user.is_active:
#         auth.login(request, user)
#         return HttpResponseRedirect('/')
#     else:
#         return HttpResponseRedirect("/login/")

def home_view(request):
    return render(request, 'home/dashboard.html')