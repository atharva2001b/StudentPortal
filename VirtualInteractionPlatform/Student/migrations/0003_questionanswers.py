# Generated by Django 3.2.4 on 2021-06-15 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_auto_20210615_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionanswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(default='', max_length=300)),
                ('Answers', models.CharField(default='', max_length=300)),
                ('rollnumber', models.IntegerField(default=0)),
                ('teacher_id', models.IntegerField(default=0)),
            ],
        ),
    ]
