# Generated by Django 3.0 on 2020-01-29 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20200129_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtask',
            name='Tpname',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.addProject'),
            preserve_default=False,
        ),
    ]