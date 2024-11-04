# Generated by Django 5.0.7 on 2024-10-14 07:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_delete_addcourse'),
        ('facultyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(choices=[('AOOP', 'Advanced Object Oriented Programming'), ('PFSD', 'Python FUll Stack Development')], max_length=50)),
                ('marks', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.studentlist')),
            ],
        ),
    ]