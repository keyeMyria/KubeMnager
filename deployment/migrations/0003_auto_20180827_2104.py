# Generated by Django 2.1 on 2018-08-27 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0002_auto_20180827_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deployment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
