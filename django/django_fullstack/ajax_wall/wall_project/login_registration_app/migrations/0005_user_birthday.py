# Generated by Django 2.2 on 2020-02-16 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration_app', '0004_remove_user_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(default='2000-04-01'),
        ),
    ]
