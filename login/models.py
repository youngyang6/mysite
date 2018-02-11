from django.db import models

# Create your models here.

class User(models.Model):

    gender = (
        ('male','男'),
        ('female','女'),
    )

    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32,choices=gender,default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class Project(models.Model):
    name = models.CharField(max_length=128,unique=True)


    def __str__(self):
        return self.name

class Case(models.Model):
    user = models.ForeignKey('User',on_delete=models.PROTECT)
    project = models.ForeignKey('Project',on_delete=models.PROTECT)
    casenumber = models.CharField(max_length=128,unique=True)
    casename = models.CharField(max_length=256,unique=True)
    precondition = models.CharField(max_length=512)
    step = models.CharField(max_length=512,unique=True)
    expectresults = models.CharField(max_length=512,unique=True)
    createtime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.casename
