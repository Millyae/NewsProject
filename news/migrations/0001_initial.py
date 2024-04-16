# Generated by Django 5.0.4 on 2024-04-13 22:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255, unique=True)),
                ('content', models.TextField(default='')),
                ('author', models.CharField(default='', max_length=40)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]
