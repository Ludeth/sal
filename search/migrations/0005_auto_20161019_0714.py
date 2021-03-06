# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-19 14:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import search.current_user


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('search', '0004_auto_20161019_0657'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unsaved Search 2016-10-19 14:13:48.222252+00:00', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('save_search', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(default=search.current_user.get_current_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='search',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='searchgroup',
            name='search',
        ),
        migrations.DeleteModel(
            name='Search',
        ),
        migrations.AddField(
            model_name='searchgroup',
            name='saved_search',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='search.SavedSearch'),
            preserve_default=False,
        ),
    ]
