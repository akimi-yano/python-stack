# Generated by Django 2.2 on 2020-02-16 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_books_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='Not much to tell'),
            preserve_default=False,
        ),
    ]
