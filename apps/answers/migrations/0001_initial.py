# Generated by Django 5.0.1 on 2024-02-05 06:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tests', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keys', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.block')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerScience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keys', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('science', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.science')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
