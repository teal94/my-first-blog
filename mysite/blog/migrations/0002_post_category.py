# Generated by Django 2.0.13 on 2019-05-16 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]