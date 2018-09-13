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
        team_names.append(leaguedata['standings'][0]['table'][i]['team']['name'])
    # team rankings list
    team_posits = []
    for i in range(numTeams):
        team_posits.append(leaguedata['standings'][0]['table'][i]['position'])
    # team matches played list
    team_mp = []
    for i in range(numTeams):
        team_mp.append(leaguedata['standings'][0]['table'][i]['playedGames'])
    # team wins list
    team_wins = []
    for i in range(numTeams):
        team_wins.append(leaguedata['standings'][0]['table'][i]['won'])
    # team draws list
    team_draw = []
    for i in range(numTeams):
        team_draw.append(leaguedata['standings'][0]['table'][i]['draw'])
    # team losses list
    team_loss = []
    for i in range(numTeams):
        team_loss.append(leaguedata['standings'][0]['table'][i]['lost'])
    # team goals for list
    team_gf = []
    for i in range(numTeams):
        team_gf.append(leaguedata['standings'][0]['table'][i]['goalsFor'])
    # team goals against list
    team_ga = []
    for i in range(numTeams):
        team_ga.append(leaguedata['standings'][0]['table'][i]['goalsAgainst'])
    # team goal differential list
    team_gd = []
    for i in range(numTeams):
        team_gd.append(leaguedata['standings'][0]['table'][i]['goalDifference'])
    # team points list
    team_points = []
    for i in range(numTeams):
        team_points.append(leaguedata['standings'][0]['table'][i]['points'])

    table = []
    for N, P, M, W, D, L, GF, GA, GD, PI in zip(team_names, team_posits, team_mp, team_wins, team_draw, team_loss, team_gf, team_ga, team_gd, team_points):
        table.append([N, P, M, W, D, L, GF, GA, GD, PI])

    return render(request, 'tables/league_table.html', {
        'matchday' : leaguedata['season']['currentMatchday'],
        'leagueCaption' : leaguedata['competition']['name'],
        'table' : table
    })

def bundesliga_1(request):
    league_url = 'http://api.football-data.org/v2/competitions/2002/standings'
    return get_data(league_url, 18, request)

def premier_league(request):
    league_url = 'http://api.football-data.org/v2/competitions/2021/standings'
    return get_data(league_url, 20, request)

def ligue_one(request):
    league_url = 'http://api.football-data.org/v2/competitions/2015/standings'
    return get_data(league_url, 20, request)

def serie_a(request):
    league_url = 'http://api.football-data.org/v2/competitions/2019/standings'
    return get_data(league_url, 20, request)

def laliga(request):
    league_url = 'http://api.football-data.org/v2/competitions/2014/standings'
    return get_data(league_url, 20, request)
