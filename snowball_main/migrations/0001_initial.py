# Generated by Django 4.0.4 on 2023-06-23 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WindowModel',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('url', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('top', models.IntegerField(default=0)),
                ('left', models.IntegerField(default=0)),
            ],
        ),
    ]