# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-01 13:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_abc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abc',
            old_name='team11_p1',
            new_name='team1_player1',
        ),
        migrations.RenameField(
            model_name='abc',
            old_name='team11_p2',
            new_name='team1_player2',
        ),
        migrations.RenameField(
            model_name='abc',
            old_name='team11_s',
            new_name='team1_score',
        ),
        migrations.RenameField(
            model_name='abc',
            old_name='team12_p1',
            new_name='team2_player1',
        ),
        migrations.RenameField(
            model_name='abc',
            old_name='team12_p2',
            new_name='team2_player2',
        ),
        migrations.RenameField(
            model_name='abc',
            old_name='team12_s',
            new_name='team2_score',
        ),
    ]