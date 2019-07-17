# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-16 00:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN_APP', '0001_initial'),
        ('BOOK_APP', '0003_auto_20190715_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authors',
            name='contributor',
        ),
        migrations.AddField(
            model_name='authors',
            name='contributor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='added_author', to='LOGIN_APP.Users'),
        ),
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.ManyToManyField(related_name='books', to='BOOK_APP.Authors'),
        ),
        migrations.RemoveField(
            model_name='books',
            name='contributor',
        ),
        migrations.AddField(
            model_name='books',
            name='contributor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='added_book', to='LOGIN_APP.Users'),
        ),
    ]