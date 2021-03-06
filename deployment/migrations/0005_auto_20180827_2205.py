# Generated by Django 2.1 on 2018-08-27 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0004_auto_20180827_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deployment',
            name='available',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='desired',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='unavailable',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='updated',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
