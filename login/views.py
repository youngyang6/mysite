from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from .models import User,Project,Case
from .forms import UserForm,CreateForm
#from django.contrib.auth.decorators import login_required

# Create your views here.

#@login_required
def index(request):
    user = request.session.get('user_name','')
    case_list = Case.objects.filter(user_id=User.objects.get(name=user))
    return render(request,'login/index.html',{"cases":case_list})


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

def create_case(request):
    #user = request.session.get('user_name','')
    if request.method == "POST":
        create_form = CreateForm(request.POST)
        if create_form.is_valid():
            user = create_form.cleaned_data['user']
            project = create_form.cleaned_data['project']
            casenumber = create_form.cleaned_data['casenumber']
            casename = create_form.cleaned_data['casename']
            precondition = create_form.cleaned_data['precondition']
            step = create_form.cleaned_data['step']
            expectresults = create_form.cleaned_data['expectresults']

            new_case = Case()
            new_case.user = User.objects.get(name=user)
            new_case.project = Project.objects.get(name=project)
            new_case.casenumber = casenumber
            new_case.casename = casename
            new_case.precondition = precondition
            new_case.step = step
            new_case.expectresults = expectresults
            new_case.save()
            return redirect('/index/')
    create_form = CreateForm(request.POST)
    return render(request,'login/create_case.html',locals())


def logout(request):
    if not request.session.get('is_login',None):
        return redirect("/login/")

    request.session.flush()
    return redirect("/login/")
