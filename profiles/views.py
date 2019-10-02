from django.shortcuts import render
from django.contrib import auth
import getpass
from django.contrib.auth.models import User
# Create your views here.
def login_view(request):
    """
    Login View
    :param request:
    :return:
    """
    get_user = getpass.getuser()
    try:
        data = User.objects.get(username=get_user)
        if request.method == 'POST':
            username = get_user
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/')
            else:
                messages.error(request,'Invalid UserName or Password')
                return render(request, 'profile/login.html', context=context)
        else:
            return render(request, 'profile/login.html', context=context)
    except Exception as e:
        if request.method == 'POST':
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/')
            else:
                messages.error(request,'Invalid UserName or Password')
                return render(request, 'profile/login_custom.html')
        else:
            return render(request, 'profile/login_custom.html')