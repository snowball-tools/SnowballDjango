# Generated by Django 4.0.4 on 2023-06-12 03:04

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('snowball_documentation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentation',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
