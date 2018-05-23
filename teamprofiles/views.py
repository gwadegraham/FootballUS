from django.http import HttpResponse
from django.shortcuts import render
import requests
from datetime import datetime

# Create your views here.
def get_team_data(team_url, fixture_url, player_url, request):
	headers = {'X-Auth-Token' : 'f097556025964ad88a20c752b96acca9'}
	# get team general data
	team_response = requests.get(team_url, headers=headers)
	teamdata = team_response.json()
	# get team fixtures data
	fixture_response = requests.get(fixture_url, headers=headers)
	fixturedata = fixture_response.json()
	# get team players data
	player_response = requests.get(player_url, headers=headers)
	playerdata = player_response.json()
	# get number of fixtures (goal is to get previous num_fixtures)
	fix_counter = int(fixturedata['count']) - 1
	num_fixtures = 5
	# get number of players
	num_players = int(playerdata['count'])
	num_div = num_players/2
	num_play_1 = num_div - 1
	num_play_2 = num_players - 1
	# match dates list
	match_dates = []
	for i in range(fix_counter, (fix_counter-num_fixtures), -1):
		date = datetime.strptime(fixturedata['fixtures'][i]['date'], "%Y-%m-%dT%H:%M:%SZ")
		format_date = date.strftime('%A %b %d, %Y')
		match_dates.append(format_date)
	# home team name list
	home_teams = []
	for i in range(fix_counter, (fix_counter-num_fixtures), -1):
	    home_teams.append(fixturedata['fixtures'][i]['homeTeamName'])
	# away team name list
	away_teams = []
	for i in range(fix_counter, (fix_counter-num_fixtures), -1):
	    away_teams.append(fixturedata['fixtures'][i]['awayTeamName'])
	# goals home team list
	home_goals = []
	for i in range(fix_counter, (fix_counter-num_fixtures), -1):
	    home_goals.append(fixturedata['fixtures'][i]['result']['goalsHomeTeam'])
	# goals away team list
	away_goals = []
	for i in range(fix_counter, (fix_counter-num_fixtures), -1):
	    away_goals.append(fixturedata['fixtures'][i]['result']['goalsAwayTeam'])
	# player names list 1
	play_names_1 = []
	for i in range(0,num_play_1):
	    play_names_1.append(playerdata['players'][i]['name'])
	# player names list 2
	play_names_2 = []
	for i in range(num_div, num_play_2):
	    play_names_2.append(playerdata['players'][i]['name'])
	# player position list 1
	play_pos_1 = []
	for i in range(0,num_play_1):
	    play_pos_1.append(playerdata['players'][i]['position'])
	# player position list 2
	play_pos_2 = []
	for i in range(num_div, num_play_2):
	    play_pos_2.append(playerdata['players'][i]['position'])
	# player number list 1
	play_num_1 = []
	for i in range(0,num_play_1):
	    play_num_1.append(playerdata['players'][i]['jerseyNumber'])
	# player number list 2
	play_num_2 = []
	for i in range(num_div, num_play_2):
	    play_num_2.append(playerdata['players'][i]['jerseyNumber'])
	# player nationality list 1
	play_nat_1 = []
	for i in range(0,num_play_1):
	    play_nat_1.append(playerdata['players'][i]['nationality'])
	# player nationality list 2
	play_nat_2 = []
	for i in range(num_div, num_play_2):
	    play_nat_2.append(playerdata['players'][i]['nationality'])

	fixtureInfo = []
	for D, H, A, HG, AG in zip(match_dates, home_teams, away_teams, home_goals, away_goals):
		fixtureInfo.append([D, H, A, HG, AG])

	playerInfo1 = []
	for N, P, NU, NA in zip(play_names_1, play_pos_1, play_num_1, play_nat_1):
		playerInfo1.append([N, P, NU, NA])

	playerInfo2 = []
	for N, P, NU, NA in zip(play_names_2, play_pos_2, play_num_2, play_nat_2):
		playerInfo2.append([N, P, NU, NA])

	return render(request, 'teamprofiles/base_team_profile.html', {
		'teamName' : teamdata['name'],
		'teamCrest' : teamdata['crestUrl'],
		'fixtureInfo' : fixtureInfo,
		'playerInfo1' : playerInfo1,
		'playerInfo2' : playerInfo2
	})

def borussia_dortmund(request):
	team_url = 'http://api.football-data.org/v1/teams/4'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)