# Generated by Django 3.0 on 2020-01-21 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userlogin',
            table='login',
        ),
    ]