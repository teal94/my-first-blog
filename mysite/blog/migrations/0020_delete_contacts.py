# Generated by Django 2.0.13 on 2019-05-19 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_contacts'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contacts',
        ),
    ]