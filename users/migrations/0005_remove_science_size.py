# Generated by Django 5.0.1 on 2024-01-14 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_checktestanswers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='science',
            name='size',
        ),
    ]
