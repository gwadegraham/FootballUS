# - *- coding: utf- 8 - *-

from django.conf.urls import url
from . import views

urlpatterns = [
	# Bundesliga url patterns
    url(r'^Borussia Dortmund$', views.borussia_dortmund, name="borussia_dortmund"),
    url(r'^FC Bayern M[\w|\W]nchen$', views.bayern_munich, name="bayern_munich"),
    url(r'^FC Schalke 04$', views.schalke, name="schalke"),
    url(r'^TSG 1899 Hoffenheim$', views.hoffenheim, name="hoffenheim"),
    url(r'^Bayer Leverkusen$', views.bayer_leverkusen, name="bayer_leverkusen"),
    url(r'^Red Bull Leipzig$', views.red_bull_leipzig, name="red_bull_leipzig"),
    url(r'^VfB Stuttgart$', views.vfb_stuttgart, name="vfb_stuttgart"),
    url(r'^Eintracht Frankfurt$', views.eintracht_frankfurt, name="eintracht_frankfurt"),
    url(r'^Bor. M[\w|\W]nchengladbach$', views.borussia_monchengladbach, name="borussia_monchengladbach"),
    url(r'^Hertha BSC$', views.hertha_berlin, name="hertha_berlin"),
    url(r'^Werder Bremen$', views.werder_bremen, name="werder_bremen"),
    url(r'^FC Augsburg$', views.fc_augsburg, name="fc_augsburg"),
    url(r'^Hannover 96$', views.hannover_96, name="hannover_96"),
    url(r'^1. FSV Mainz 05$', views.fsv_mainz_05, name="fsv_mainz_05"),
    url(r'^SC Freiburg$', views.sc_freiburg, name="sc_freiburg"),
    url(r'^VfL Wolfsburg$', views.vfl_wolfsburg, name="vfl_wolfsburg"),
    url(r'^Hamburger SV$', views.hamburger_sv, name="hamburger_sv"),
    url(r'^1. FC K[\w|\W]ln$', views.fc_koln, name="fc_koln"),
    # Premier League url patterns
    url(r'^Manchester City FC$', views.manchester_city, name="manchester_city"),
    url(r'^Manchester United FC$', views.manchester_united, name="manchester_united"),
    url(r'^Tottenham Hotspur FC$', views.tottenham_hotspur, name="tottenham_hotspur"),
    url(r'^Liverpool FC$', views.liverpool, name="liverpool"),
    url(r'^Chelsea FC$', views.chelsea, name="chelsea"),
    url(r'^Arsenal FC$', views.arsenal, name="arsenal"),
    url(r'^Burnley FC$', views.burnley, name="burnley"),
    url(r'^Everton FC$', views.everton, name="everton"),
    url(r'^Leicester City FC$', views.leicester_city, name="leicester_city"),
    url(r'^Newcastle United FC$', views.newcastle_united, name="newcastle_united"),
    url(r'^Crystal Palace FC$', views.crystal_palace, name="crystal_palace"),
    url(r'^AFC Bournemouth$', views.afc_bournemouth, name="afc_bournemouth"),
    url(r'^West Ham United FC$', views.west_ham_united, name="west_ham_united"),
    url(r'^Watford FC$', views.watford, name="watford"),
    url(r'^Brighton & Hove Albion$', views.brighton_hove_albion, name="brighton_hove_albion"),
    url(r'^Huddersfield Town$', views.huddersfield_town, name="huddersfield_town"),
    url(r'^Southampton FC$', views.southampton, name="southampton"),
    url(r'^Swansea City FC$', views.swansea_city, name="swansea_city"),
    url(r'^Stoke City FC$', views.stoke_city, name="stoke_city"),
    url(r'^West Bromwich Albion FC$', views.west_bromwich_albion, name="west_bromwich_albion"),
    # Ligue 1 url patterns
    url(r'^Paris Saint-Germain$', views.paris_saint_germain, name="paris_saint_germain"),
    url(r'^AS Monaco FC$', views.as_monaco, name="as_monaco"),
    url(r'^Olympique Lyonnais$', views.olympique_lyonnais, name="olympique_lyonnais"),
    url(r'^Olympique de Marseille$', views.olympique_de_marseille, name="olympique_de_marseille"),
    url(r'^Stade Rennais FC$', views.stade_rennais, name="stade_rennais"),
    url(r'^FC Girondins de Bordeaux$', views.girondins_de_bordeaux, name="girondins_de_bordeaux"),
    url(r'^AS Saint-[\w|\W]tienne$', views.as_saint_etienne, name="as_saint_etienne"),
    url(r'^OGC Nice$', views.ogc_nice, name="ogc_nice"),
    url(r'^FC Nantes$', views.nantes, name="nantes"),
    url(r'^Montpellier H[\w|\W]rault SC$', views.montpellier_herault, name="montpellier_herault"),
    url(r'^Dijon FCO$', views.dijon_fco, name="dijon_fco"),
    url(r'^EA Guingamp$', views.ea_guingamp, name="ea_guingamp"),
    url(r'^Amiens SC$', views.amiens, name="amiens"),
    url(r'^Angers SCO$', views.angers, name="angers"),
    url(r'^RC Strasbourg Alsace$', views.rc_strasbourg_alsace, name="rc_strasbourg_alsace"),
    url(r'^SM Caen$', views.sm_caen, name="sm_caen"),
    url(r'^OSC Lille$', views.osc_lille, name="osc_lille"),
    url(r'^Toulouse FC$', views.toulouse, name="toulouse"),
    url(r'^ES Troyes AC$', views.es_troyes_ac, name="es_troyes_ac"),
    url(r'^FC Metz$', views.metz, name="metz"),
]







