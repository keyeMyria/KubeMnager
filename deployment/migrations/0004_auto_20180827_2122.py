# Generated by Django 2.1 on 2018-08-27 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0003_auto_20180827_2104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deployment',
            old_name='deployment_name',
            new_name='name',
        ),
    ]
