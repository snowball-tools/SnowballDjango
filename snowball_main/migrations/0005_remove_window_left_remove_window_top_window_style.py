# Generated by Django 4.0.4 on 2023-07-02 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snowball_main', '0004_alter_window_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='window',
            name='left',
        ),
        migrations.RemoveField(
            model_name='window',
            name='top',
        ),
        migrations.AddField(
            model_name='window',
            name='style',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
