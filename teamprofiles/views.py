from django.http import HttpResponse
from django.shortcuts import render
import requests
from datetime import datetime

# list of mobile User Agents
mobile_uas = [
	'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
	'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
	'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
	'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
	'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
	'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
	'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
	'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
	'wapr','webc','winw','winw','xda','xda-'
	]

mobile_ua_hints = [ 'SymbianOS', 'Opera Mini', 'iPhone' ]


def mobileBrowser(request):
    ''' Super simple device detection, returns True for mobile devices '''

    mobile_browser = False
    ua = request.META['HTTP_USER_AGENT'].lower()[0:4]

    if (ua in mobile_uas):
        mobile_browser = True
    else:
        for hint in mobile_ua_hints:
            if request.META['HTTP_USER_AGENT'].find(hint) > 0:
                mobile_browser = True

    return mobile_browser

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
	if (num_fixtures > fixturedata['count']):
		num_fixtures = fixturedata['count']
	# get number of players
	num_players = int(len(playerdata['squad']))
	num_div = num_players/2
	# match dates list
	match_dates = []
	for i in range(fix_counter, (fix_counter-num_fixtures), -1):
		date = datetime.strptime(fixturedata['matches'][i]['utcDate'], "%Y-%m-%dT%H:%M:%SZ")
		format_date = date.strftime('%A %b %d, %Y')
		match_dates.append(format_date)
	# home team name list
	home_teams = []
	for i in range(fix_counter, (fix_counter-num_fixtures), -1):
	    home_teams.append(fixturedata['matches'][i]['homeTeam']['name'])
	# away team name list
	away_teams = []
	for i in range(fix_counter, (fix_counter-num_fixtures), -1):
	    away_teams.append(fixturedata['matches'][i]['awayTeam']['name'])
	# goals home team list
	home_goals = []
	for i in range(fix_counter, (fix_counter-num_fixtures), -1):
	    home_goals.append(fixturedata['matches'][i]['score']['fullTime']['homeTeam'])
	# goals away team list
	away_goals = []
	for i in range(fix_counter, (fix_counter-num_fixtures), -1):
	    away_goals.append(fixturedata['matches'][i]['score']['fullTime']['awayTeam'])
	# player names list 1
	play_names_1 = []
	for i in range(0,num_div):
		if playerdata['squad'][i]['role'] != "COACH":
			play_names_1.append(playerdata['squad'][i]['name'])
		else:
			0+0
	# player names list 2
	play_names_2 = []
	for i in range(num_div, num_players):
		if playerdata['squad'][i]['role'] != "COACH":
			play_names_2.append(playerdata['squad'][i]['name'])
		else:
			0+0
	# player position list 1
	play_pos_1 = []
	for i in range(0,num_div):
		if playerdata['squad'][i]['role'] != "COACH":
			play_pos_1.append(playerdata['squad'][i]['position'])
		else:
			0+0
	# player position list 2
	play_pos_2 = []
	for i in range(num_div, num_players):
		if playerdata['squad'][i]['role'] != "COACH":
			play_pos_2.append(playerdata['squad'][i]['position'])
		else:
			0+0
	# player nationality list 1
	play_nat_1 = []
	for i in range(0,num_div):
		if playerdata['squad'][i]['role'] != "COACH":
			play_nat_1.append(playerdata['squad'][i]['nationality'])
		else:
			0+0
	# player nationality list 2
	play_nat_2 = []
	for i in range(num_div, num_players):
		if playerdata['squad'][i]['role'] != "COACH":
			play_nat_2.append(playerdata['squad'][i]['nationality'])
		else:
			0+0
	# finding the coach
	coach = []
	for i in range(0, num_players):
		if playerdata['squad'][i]['role'] == "COACH":
			coach.append(playerdata['squad'][i]['name'])
			coach.append("Coach")
			coach.append(playerdata['squad'][i]['nationality'])
		else:
			0+0

	fixtureInfo = []
	for D, H, A, HG, AG in zip(match_dates, home_teams, away_teams, home_goals, away_goals):
		fixtureInfo.append([D, H, A, HG, AG])

	playerInfo1 = []
	for N, P, NA in zip(play_names_1, play_pos_1, play_nat_1):
		playerInfo1.append([N, P, NA])

	playerInfo2 = []
	for N, P, NA in zip(play_names_2, play_pos_2, play_nat_2):
		playerInfo2.append([N, P, NA])

	if mobileBrowser(request):
            return render(request, 'teamprofiles/m_base_team_profile.html', {
				'teamName' : teamdata['name'],
				'teamCrest' : teamdata['crestUrl'],
				'fixtureInfo' : fixtureInfo,
				'playerInfo1' : playerInfo1,
				'playerInfo2' : playerInfo2,
				'coachInfo' : coach
			})
	else:
            return render(request, 'teamprofiles/base_team_profile.html', {
				'teamName' : teamdata['name'],
				'teamCrest' : teamdata['crestUrl'],
				'fixtureInfo' : fixtureInfo,
				'playerInfo1' : playerInfo1,
				'playerInfo2' : playerInfo2,
				'coachInfo' : coach
			})

	return render(request, 'teamprofiles/base_team_profile.html', {
		'teamName' : teamdata['name'],
		'teamCrest' : teamdata['crestUrl'],
		'fixtureInfo' : fixtureInfo,
		'playerInfo1' : playerInfo1,
		'playerInfo2' : playerInfo2,
		'coachInfo' : coach
	})

# ------------------------------- #
#         Bundesliga Views        #
# ------------------------------- #

def borussia_dortmund(request):
	team_url = 'http://api.football-data.org/v2/teams/4'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def bayern_munich(request):
	team_url = 'http://api.football-data.org/v2/teams/5'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def schalke(request):
	team_url = 'http://api.football-data.org/v2/teams/6'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def hoffenheim(request):
	team_url = 'http://api.football-data.org/v2/teams/2'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def bayer_leverkusen(request):
	team_url = 'http://api.football-data.org/v2/teams/3'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def red_bull_leipzig(request):
	team_url = 'http://api.football-data.org/v2/teams/721'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def vfb_stuttgart(request):
	team_url = 'http://api.football-data.org/v2/teams/10'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def eintracht_frankfurt(request):
	team_url = 'http://api.football-data.org/v2/teams/19'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def borussia_monchengladbach(request):
	team_url = 'http://api.football-data.org/v2/teams/18'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def hertha_berlin(request):
	team_url = 'http://api.football-data.org/v2/teams/9'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def werder_bremen(request):
	team_url = 'http://api.football-data.org/v2/teams/12'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def fc_augsburg(request):
	team_url = 'http://api.football-data.org/v2/teams/16'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def hannover_96(request):
	team_url = 'http://api.football-data.org/v2/teams/8'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def fsv_mainz_05(request):
	team_url = 'http://api.football-data.org/v2/teams/15'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def sc_freiburg(request):
	team_url = 'http://api.football-data.org/v2/teams/17'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def vfl_wolfsburg(request):
	team_url = 'http://api.football-data.org/v2/teams/11'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def hamburger_sv(request):
	team_url = 'http://api.football-data.org/v2/teams/7'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def fc_koln(request):
	team_url = 'http://api.football-data.org/v2/teams/1'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)


# ------------------------------- #
#       Premier League Views      #
# ------------------------------- #

def manchester_city(request):
	team_url = 'http://api.football-data.org/v2/teams/65'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def manchester_united(request):
	team_url = 'http://api.football-data.org/v2/teams/66'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def tottenham_hotspur(request):
	team_url = 'http://api.football-data.org/v2/teams/73'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def liverpool(request):
	team_url = 'http://api.football-data.org/v2/teams/64'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def chelsea(request):
	team_url = 'http://api.football-data.org/v2/teams/61'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def arsenal(request):
	team_url = 'http://api.football-data.org/v2/teams/57'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def burnley(request):
	team_url = 'http://api.football-data.org/v2/teams/328'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def everton(request):
	team_url = 'http://api.football-data.org/v2/teams/62'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def leicester_city(request):
	team_url = 'http://api.football-data.org/v2/teams/338'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def newcastle_united(request):
	team_url = 'http://api.football-data.org/v2/teams/67'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def crystal_palace(request):
	team_url = 'http://api.football-data.org/v2/teams/354'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def afc_bournemouth(request):
	team_url = 'http://api.football-data.org/v2/teams/1044'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def west_ham_united(request):
	team_url = 'http://api.football-data.org/v2/teams/563'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def watford(request):
	team_url = 'http://api.football-data.org/v2/teams/346'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def brighton_hove_albion(request):
	team_url = 'http://api.football-data.org/v2/teams/397'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def huddersfield_town(request):
	team_url = 'http://api.football-data.org/v2/teams/394'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def southampton(request):
	team_url = 'http://api.football-data.org/v2/teams/340'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def swansea_city(request):
	team_url = 'http://api.football-data.org/v2/teams/72'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def stoke_city(request):
	team_url = 'http://api.football-data.org/v2/teams/70'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def west_bromwich_albion(request):
	team_url = 'http://api.football-data.org/v2/teams/74'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

# ------------------------------- #
#          Ligue 1 Views          #
# ------------------------------- #

def paris_saint_germain(request):
	team_url = 'http://api.football-data.org/v2/teams/524'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def as_monaco(request):
	team_url = 'http://api.football-data.org/v2/teams/548'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def olympique_lyonnais(request):
	team_url = 'http://api.football-data.org/v2/teams/523'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def olympique_de_marseille(request):
	team_url = 'http://api.football-data.org/v2/teams/516'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def stade_rennais(request):
	team_url = 'http://api.football-data.org/v2/teams/529'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def girondins_de_bordeaux(request):
	team_url = 'http://api.football-data.org/v2/teams/526'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def as_saint_etienne(request):
	team_url = 'http://api.football-data.org/v2/teams/527'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def ogc_nice(request):
	team_url = 'http://api.football-data.org/v2/teams/522'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def nantes(request):
	team_url = 'http://api.football-data.org/v2/teams/543'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def montpellier_herault(request):
	team_url = 'http://api.football-data.org/v2/teams/518'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def dijon_fco(request):
	team_url = 'http://api.football-data.org/v2/teams/528'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def ea_guingamp(request):
	team_url = 'http://api.football-data.org/v2/teams/538'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def amiens(request):
	team_url = 'http://api.football-data.org/v2/teams/530'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def angers(request):
	team_url = 'http://api.football-data.org/v2/teams/532'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def rc_strasbourg_alsace(request):
	team_url = 'http://api.football-data.org/v2/teams/576'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def sm_caen(request):
	team_url = 'http://api.football-data.org/v2/teams/514'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def osc_lille(request):
	team_url = 'http://api.football-data.org/v2/teams/521'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def toulouse(request):
	team_url = 'http://api.football-data.org/v2/teams/511'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def es_troyes_ac(request):
	team_url = 'http://api.football-data.org/v2/teams/531'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def metz(request):
	team_url = 'http://api.football-data.org/v2/teams/545'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

# ------------------------------- #
#          Serie A Views          #
# ------------------------------- #

def juventus_turin(request):
	team_url = 'http://api.football-data.org/v2/teams/109'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def ssc_napoli(request):
	team_url = 'http://api.football-data.org/v2/teams/113'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def as_roma(request):
	team_url = 'http://api.football-data.org/v2/teams/100'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def ss_lazio(request):
	team_url = 'http://api.football-data.org/v2/teams/110'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def inter_milan(request):
	team_url = 'http://api.football-data.org/v2/teams/108'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def ac_milan(request):
	team_url = 'http://api.football-data.org/v2/teams/98'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def atalanta_bc(request):
	team_url = 'http://api.football-data.org/v2/teams/102'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def acf_fiorentina(request):
	team_url = 'http://api.football-data.org/v2/teams/99'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def torino_fc(request):
	team_url = 'http://api.football-data.org/v2/teams/586'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def uc_sampdoria(request):
	team_url = 'http://api.football-data.org/v2/teams/584'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def us_sassuolo_calcio(request):
	team_url = 'http://api.football-data.org/v2/teams/471'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def genoa_cfc(request):
	team_url = 'http://api.football-data.org/v2/teams/107'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def udinese_calcio(request):
	team_url = 'http://api.football-data.org/v2/teams/115'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def ac_chievo_verona(request):
	team_url = 'http://api.football-data.org/v2/teams/106'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def bologna_fc(request):
	team_url = 'http://api.football-data.org/v2/teams/103'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def cagliari_calcio(request):
	team_url = 'http://api.football-data.org/v2/teams/104'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def spal_ferrara(request):
	team_url = 'http://api.football-data.org/v2/teams/1107'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def fc_crotone(request):
	team_url = 'http://api.football-data.org/v2/teams/472'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def hellas_verona_fc(request):
	team_url = 'http://api.football-data.org/v2/teams/450'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def benevento_calcio(request):
	team_url = 'http://api.football-data.org/v2/teams/1106'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

# ------------------------------- #
#          LaLiga Views           #
# ------------------------------- #

def barcelona(request):
	team_url = 'http://api.football-data.org/v2/teams/81'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def atletico_madrid(request):
	team_url = 'http://api.football-data.org/v2/teams/78'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def real_madrid(request):
	team_url = 'http://api.football-data.org/v2/teams/86'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def valencia(request):
	team_url = 'http://api.football-data.org/v2/teams/95'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def villarreal(request):
	team_url = 'http://api.football-data.org/v2/teams/94'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def real_betis(request):
	team_url = 'http://api.football-data.org/v2/teams/90'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def sevilla(request):
	team_url = 'http://api.football-data.org/v2/teams/559'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def getafe(request):
	team_url = 'http://api.football-data.org/v2/teams/82'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def sd_eibar(request):
	team_url = 'http://api.football-data.org/v2/teams/278'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def girona(request):
	team_url = 'http://api.football-data.org/v2/teams/298'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def real_sociedad(request):
	team_url = 'http://api.football-data.org/v2/teams/92'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def celta_de_vigo(request):
	team_url = 'http://api.football-data.org/v2/teams/558'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def espanyol(request):
	team_url = 'http://api.football-data.org/v2/teams/80'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def deportivo_alaves(request):
	team_url = 'http://api.football-data.org/v2/teams/263'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def levante_ud(request):
	team_url = 'http://api.football-data.org/v2/teams/88'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def athletic_club(request):
	team_url = 'http://api.football-data.org/v2/teams/77'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def leganes(request):
	team_url = 'http://api.football-data.org/v2/teams/745'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def deportivo_la_coruna(request):
	team_url = 'http://api.football-data.org/v2/teams/560'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def las_palmas(request):
	team_url = 'http://api.football-data.org/v2/teams/275'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)

def malaga(request):
	team_url = 'http://api.football-data.org/v2/teams/84'
	fixture_url = team_url + '/matches?status=FINISHED'
	player_url = team_url
	return get_team_data(team_url, fixture_url, player_url, request)
