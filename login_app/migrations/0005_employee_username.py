# Generated by Django 4.0.5 on 2022-07-29 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0004_remove_employee_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
