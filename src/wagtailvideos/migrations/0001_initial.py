# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-02 01:50
from __future__ import absolute_import, print_function, unicode_literals

import django.db.models.deletion
import taggit.managers
import wagtail.models
import wagtail.search.index
from django.conf import settings
from django.db import migrations, models

import src.wagtailvideos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('file', models.ImageField(height_field='height', upload_to=src.wagtailvideos.models.get_upload_to, verbose_name='file', width_field='width')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('file_size', models.PositiveIntegerField(editable=False, null=True)),
                ('collection', models.ForeignKey(default=wagtail.models.get_root_collection_id, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Collection', verbose_name='collection')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text=None, through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags')),
                ('uploaded_by_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='uploaded by user')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
