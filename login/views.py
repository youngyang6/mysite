from django.shortcuts import render
from django.shortcuts import redirect
from .models import User
from .forms import UserForm

# Create your views here.


def index(request):
    pass
    return render(request,'login/index.html')


def login(request):
    if request.method == "POST":
        login_form = UserForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
                if user.password == password:
                    return redirect("/index/")
                else:
                    message = "密码不正确"
            except:
                message = "用户不存在"
        return render(request, 'login/login.html', locals())
    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    pass
    return render(request,'login/register.html')


def logout(request):
    pass
    return redirect("/index/")
