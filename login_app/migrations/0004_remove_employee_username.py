# Generated by Django 4.0.5 on 2022-07-29 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_alter_employee_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='username',
        ),
    ]
