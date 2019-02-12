from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):

    username = forms.CharField(label="用户名",max_length=128,
            widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="密码",max_length=256,
            widget=forms.PasswordInput(attrs={'class':'form-control'}))
    captcha = CaptchaField(label='验证码')


class CreateForm(forms.Form):

    user = forms.CharField(label="提交人",max_length=128,
                           widget=forms.TextInput(attrs={'class':'form-control'}))

    project = forms.CharField(label="项目",max_length=128,
                              widget=forms.TextInput(attrs={'class':'form-control'}))

    casenumber = forms.CharField(label="用例编号",max_length=128,
                              widget=forms.TextInput(attrs={'class':'form-control'}))

    casename = forms.CharField(label="用例名称",max_length=256,
                              widget=forms.TextInput(attrs={'class':'form-control'}))

    precondition = forms.CharField(label="预置条件",max_length=512,
                              widget=forms.TextInput(attrs={'class':'form-control'}))

    step = forms.CharField(label="测试步骤",max_length=512,
                              widget=forms.TextInput(attrs={'class':'form-control'}))

    expectresults = forms.CharField(label="预期结果",max_length=512,
                              widget=forms.TextInput(attrs={'class':'form-control'}))