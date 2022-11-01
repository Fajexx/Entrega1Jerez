from django.urls import path

from figurines import views

app_name = "figurines"

urlpatterns =[
    path("players_list/", views.show_players, name="players-list"),
    path("national_teams_list/", views.show_national_teams, name="national-teams-list"),
    path("stadiums_list/", views.show_stadiums, name="stadiums-list")
]