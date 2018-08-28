# Generated by Django 2.1 on 2018-08-28 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deployment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('namespace', models.CharField(max_length=20)),
                ('version', models.CharField(max_length=20)),
                ('desired', models.IntegerField(default=0, null=True)),
                ('unavailable', models.IntegerField(default=0, null=True)),
                ('updated', models.IntegerField(default=0, null=True)),
                ('available', models.IntegerField(default=0, null=True)),
            ],
        ),
    ]