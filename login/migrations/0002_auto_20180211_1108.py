# Generated by Django 2.0.1 on 2018-02-11 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casenumber', models.CharField(max_length=128, unique=True)),
                ('casename', models.CharField(max_length=256, unique=True)),
                ('precondition', models.CharField(max_length=512)),
                ('step', models.CharField(max_length=512, unique=True)),
                ('expectresults', models.CharField(max_length=512, unique=True)),
                ('createtime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='login.Project'),
        ),
        migrations.AddField(
            model_name='case',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='login.User'),
        ),
    ]
