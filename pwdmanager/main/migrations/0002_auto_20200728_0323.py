# Generated by Django 2.1.4 on 2020-07-28 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='webpwd',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
