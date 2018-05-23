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
	for i in range(0,num_div):
	    play_names_1.append(playerdata['players'][i]['name'])
	# player names list 2
	play_names_2 = []
	for i in range(num_div, num_players):
	    play_names_2.append(playerdata['players'][i]['name'])
	# player position list 1
	play_pos_1 = []
	for i in range(0,num_div):
	    play_pos_1.append(playerdata['players'][i]['position'])
	# player position list 2
	play_pos_2 = []
	for i in range(num_div, num_players):
	    play_pos_2.append(playerdata['players'][i]['position'])
	# player number list 1
	play_num_1 = []
	for i in range(0,num_div):
	    play_num_1.append(playerdata['players'][i]['jerseyNumber'])
	# player number list 2
	play_num_2 = []
	for i in range(num_div, num_players):
	    play_num_2.append(playerdata['players'][i]['jerseyNumber'])
	# player nationality list 1
	play_nat_1 = []
	for i in range(0,num_div):
	    play_nat_1.append(playerdata['players'][i]['nationality'])
	# player nationality list 2
	play_nat_2 = []
	for i in range(num_div, num_players):
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

# ------------------------------- #
#         Bundesliga Views        #
# ------------------------------- #

def borussia_dortmund(request):
	team_url = 'http://api.football-data.org/v1/teams/4'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def bayern_munich(request):
	team_url = 'http://api.football-data.org/v1/teams/5'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def schalke(request):
	team_url = 'http://api.football-data.org/v1/teams/6'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def hoffenheim(request):
	team_url = 'http://api.football-data.org/v1/teams/2'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def bayer_leverkusen(request):
	team_url = 'http://api.football-data.org/v1/teams/3'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def red_bull_leipzig(request):
	team_url = 'http://api.football-data.org/v1/teams/721'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def vfb_stuttgart(request):
	team_url = 'http://api.football-data.org/v1/teams/10'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def eintracht_frankfurt(request):
	team_url = 'http://api.football-data.org/v1/teams/19'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def borussia_monchengladbach(request):
	team_url = 'http://api.football-data.org/v1/teams/18'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def hertha_berlin(request):
	team_url = 'http://api.football-data.org/v1/teams/9'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def werder_bremen(request):
	team_url = 'http://api.football-data.org/v1/teams/12'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def fc_augsburg(request):
	team_url = 'http://api.football-data.org/v1/teams/16'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def hannover_96(request):
	team_url = 'http://api.football-data.org/v1/teams/8'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def fsv_mainz_05(request):
	team_url = 'http://api.football-data.org/v1/teams/15'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def sc_freiburg(request):
	team_url = 'http://api.football-data.org/v1/teams/17'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def vfl_wolfsburg(request):
	team_url = 'http://api.football-data.org/v1/teams/11'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def hamburger_sv(request):
	team_url = 'http://api.football-data.org/v1/teams/7'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def fc_koln(request):
	team_url = 'http://api.football-data.org/v1/teams/1'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)


# ------------------------------- #
#       Premier League Views      #
# ------------------------------- #

def manchester_city(request):
	team_url = 'http://api.football-data.org/v1/teams/65'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def manchester_united(request):
	team_url = 'http://api.football-data.org/v1/teams/66'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def tottenham_hotspur(request):
	team_url = 'http://api.football-data.org/v1/teams/73'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def liverpool(request):
	team_url = 'http://api.football-data.org/v1/teams/64'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def chelsea(request):
	team_url = 'http://api.football-data.org/v1/teams/61'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def arsenal(request):
	team_url = 'http://api.football-data.org/v1/teams/57'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def burnley(request):
	team_url = 'http://api.football-data.org/v1/teams/328'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def everton(request):
	team_url = 'http://api.football-data.org/v1/teams/62'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def leicester_city(request):
	team_url = 'http://api.football-data.org/v1/teams/338'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def newcastle_united(request):
	team_url = 'http://api.football-data.org/v1/teams/67'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def crystal_palace(request):
	team_url = 'http://api.football-data.org/v1/teams/354'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def afc_bournemouth(request):
	team_url = 'http://api.football-data.org/v1/teams/1044'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def west_ham_united(request):
	team_url = 'http://api.football-data.org/v1/teams/563'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def watford(request):
	team_url = 'http://api.football-data.org/v1/teams/346'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def brighton_hove_albion(request):
	team_url = 'http://api.football-data.org/v1/teams/397'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def huddersfield_town(request):
	team_url = 'http://api.football-data.org/v1/teams/394'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def southampton(request):
	team_url = 'http://api.football-data.org/v1/teams/340'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def swansea_city(request):
	team_url = 'http://api.football-data.org/v1/teams/72'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def stoke_city(request):
	team_url = 'http://api.football-data.org/v1/teams/70'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def west_bromwich_albion(request):
	team_url = 'http://api.football-data.org/v1/teams/74'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

# ------------------------------- #
#          Ligue 1 Views          #
# ------------------------------- #

def paris_saint_germain(request):
	team_url = 'http://api.football-data.org/v1/teams/524'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def as_monaco(request):
	team_url = 'http://api.football-data.org/v1/teams/548'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def olympique_lyonnais(request):
	team_url = 'http://api.football-data.org/v1/teams/523'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def olympique_de_marseille(request):
	team_url = 'http://api.football-data.org/v1/teams/516'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def stade_rennais(request):
	team_url = 'http://api.football-data.org/v1/teams/529'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def girondins_de_bordeaux(request):
	team_url = 'http://api.football-data.org/v1/teams/526'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def as_saint_etienne(request):
	team_url = 'http://api.football-data.org/v1/teams/527'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def ogc_nice(request):
	team_url = 'http://api.football-data.org/v1/teams/522'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def nantes(request):
	team_url = 'http://api.football-data.org/v1/teams/543'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def montpellier_herault(request):
	team_url = 'http://api.football-data.org/v1/teams/518'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def dijon_fco(request):
	team_url = 'http://api.football-data.org/v1/teams/528'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def ea_guingamp(request):
	team_url = 'http://api.football-data.org/v1/teams/538'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def amiens(request):
	team_url = 'http://api.football-data.org/v1/teams/530'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def angers(request):
	team_url = 'http://api.football-data.org/v1/teams/532'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def rc_strasbourg_alsace(request):
	team_url = 'http://api.football-data.org/v1/teams/576'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def sm_caen(request):
	team_url = 'http://api.football-data.org/v1/teams/514'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def osc_lille(request):
	team_url = 'http://api.football-data.org/v1/teams/521'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def toulouse(request):
	team_url = 'http://api.football-data.org/v1/teams/511'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def es_troyes_ac(request):
	team_url = 'http://api.football-data.org/v1/teams/531'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)

def metz(request):
	team_url = 'http://api.football-data.org/v1/teams/545'
	fixture_url = team_url + '/fixtures'
	player_url = team_url + '/players'
	return get_team_data(team_url, fixture_url, player_url, request)











