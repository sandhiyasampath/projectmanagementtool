# Generated by Django 3.1.3 on 2020-12-04 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_projects_projects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='projects',
        ),
        migrations.AddField(
            model_name='projects',
            name='projects',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register.employees'),
        ),
    ]
