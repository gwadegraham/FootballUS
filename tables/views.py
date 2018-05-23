from django.http import HttpResponse
from django.shortcuts import render
import requests


def index(request):
    return render(request, 'tables/index.html')

def get_data(url,numTeams, request):
    headers = {'X-Auth-Token' : 'f097556025964ad88a20c752b96acca9'}
    response = requests.get(url, headers=headers)
    leaguedata = response.json()
    # team names list
    team_names = []
    for i in range(numTeams):
        team_names.append(leaguedata['standing'][i]['teamName'])
    # team rankings list
    team_posits = []
    for i in range(numTeams):
        team_posits.append(leaguedata['standing'][i]['position'])
    # team matches played list
    team_mp = []
    for i in range(numTeams):
        team_mp.append(leaguedata['standing'][i]['playedGames'])
    # team wins list
    team_wins = []
    for i in range(numTeams):
        team_wins.append(leaguedata['standing'][i]['wins'])
    # team draws list
    team_draw = []
    for i in range(numTeams):
        team_draw.append(leaguedata['standing'][i]['draws'])
    # team losses list
    team_loss = []
    for i in range(numTeams):
        team_loss.append(leaguedata['standing'][i]['losses'])
    # team goals for list
    team_gf = []
    for i in range(numTeams):
        team_gf.append(leaguedata['standing'][i]['goals'])
    # team goals against list
    team_ga = []
    for i in range(numTeams):
        team_ga.append(leaguedata['standing'][i]['goalsAgainst'])
    # team goal differential list
    team_gd = []
    for i in range(numTeams):
        team_gd.append(leaguedata['standing'][i]['goalDifference'])
    # team points list
    team_points = []
    for i in range(numTeams):
        team_points.append(leaguedata['standing'][i]['points'])

    table = []
    for N, P, M, W, D, L, GF, GA, GD, PI in zip(team_names, team_posits, team_mp, team_wins, team_draw, team_loss, team_gf, team_ga, team_gd, team_points):
        table.append([N, P, M, W, D, L, GF, GA, GD, PI])

    return render(request, 'tables/league_table.html', {
        'matchday' : leaguedata['matchday'],
        'leagueCaption' : leaguedata['leagueCaption'],
        'table' : table
    })

def bundesliga_1(request):
    league_url = 'http://api.football-data.org/v1/competitions/452/leagueTable'
    return get_data(league_url, 18, request)

def premier_league(request):
    league_url = 'http://api.football-data.org/v1/competitions/445/leagueTable'
    return get_data(league_url, 20, request)

def ligue_one(request):
    league_url = 'http://api.football-data.org/v1/competitions/450/leagueTable'
    return get_data(league_url, 20, request)

def serie_a(request):
    league_url = 'http://api.football-data.org/v1/competitions/456/leagueTable'
    return get_data(league_url, 20, request)

def laliga(request):
    league_url = 'http://api.football-data.org/v1/competitions/455/leagueTable'
    return get_data(league_url, 20, request)