# Generated by Django 3.2 on 2021-04-09 15:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('note', models.TextField(blank=True, max_length=1023, null=True)),
                ('comments', models.TextField(blank=True, max_length=1023, null=True)),
                ('note_status', models.CharField(choices=[('active', 'Активно'), ('delay', 'Отложено'), ('done', 'Выполнено')], default='active', max_length=16, verbose_name='Состояние')),
                ('importance_status', models.BooleanField(default=False)),
                ('public_status', models.BooleanField(default=True)),
                ('task_date_time', models.DateTimeField(default=datetime.datetime(2021, 4, 10, 15, 49, 8, 667094, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
        ),
    ]