# Generated by Django 3.2.4 on 2021-06-21 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='department',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='Teacher_password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='Teacher_userid',
            field=models.CharField(default='', max_length=20),
        ),
    ]
