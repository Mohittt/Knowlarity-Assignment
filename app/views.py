# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import abcForm, abc

def getdata(request):
    if request.method == 'POST':
        form = abcForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            o = abc(team1_player1 = form.cleaned_data['team1_player1'],
                    team1_player2 = form.cleaned_data['team1_player2'],
                    team1_score = form.cleaned_data['team1_score'],
                    team2_player1 = "Nil",
                    team2_player2 = "Nil",
                    team2_score = 0)
            o.save()
            o = abc(team1_player1 = form.cleaned_data['team2_player1'],
                    team1_player2 = form.cleaned_data['team2_player2'],
                    team1_score = form.cleaned_data['team2_score'],
                    team2_player1 = "Nil",
                    team2_player2 = "Nil",
                    team2_score = 0)
            o.save()

            return HttpResponseRedirect(reverse('polls:showdata'))
        else:
            print("Form ", form.errors)
    else:
        form = abcForm()

    return render(request, 'polls/input.html', {'form': form})

def showdata(request):
    object = abc.objects.all().order_by('-team1_score')[:10]
    return render(request, 'polls/output.html', {'object': object})


