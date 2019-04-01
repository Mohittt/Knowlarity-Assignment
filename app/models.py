# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms import ModelForm
from django.db import models

class abc(models.Model):
    team1_player1 = models.CharField(max_length=200)
    team1_player2 = models.CharField(max_length=200)
    team1_score = models.IntegerField()
    team2_player1 = models.CharField(max_length=200)
    team2_player2 = models.CharField(max_length=200)
    team2_score = models.IntegerField()

    def __str__(self):
        return self.team1_score

class abcForm(ModelForm):
    class Meta:
        model = abc
        fields = ['team1_player1', 'team1_player2', 'team1_score', 'team2_player1', 'team2_player2', 'team2_score', ]