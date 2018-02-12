from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from .models import User,Project,Case
from .forms import UserForm
#from django.contrib.auth.decorators import login_required

# Create your views here.

#@login_required
def index(request):
    pass
    return render(request,'login/index.html')


def login(request):
    if request.session.get('is_login',None):
        return redirect("/index/")
    if request.method == "POST":
        login_form = UserForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    case_list = Case.objects.filter(user_id=user.id)
                    return render(request,'login/index.html',{"cases":case_list})
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

def create_case(request):
    user = request.session.get('user_name','')
    return render(request,'login/create_case.html',{"user":user})

def logout(request):
    if not request.session.get('is_login',None):
        return redirect("/login/")

    request.session.flush()
    return redirect("/login/")
