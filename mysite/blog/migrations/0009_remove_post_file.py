# Generated by Django 2.0.13 on 2019-05-19 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190519_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='file',
        ),
    ]
