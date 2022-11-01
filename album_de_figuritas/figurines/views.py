from django.shortcuts import render
from figurines.models import Player, NationalTeam, Stadium

def show_players(request):
    players = Player.objects.all()
    context_dict = {
        "players": players

        }
    return render(
        request=request,
        context=context_dict,
        template_name='figurines/players.html'
    )

def show_national_teams(request):
    national_teams = NationalTeam.objects.all()
    context_dict = {
        "national_teams": national_teams,
        }
    return render(
        request=request,
        context=context_dict,
        template_name='figurines/national_teams.html'
    )

def show_stadiums(request):
    stadiums = Stadium.objects.all()
    context_dict = {
        "stadiums": stadiums
        }
    return render(
        request=request,
        context=context_dict,
        template_name='figurines/stadiums.html'
    )
