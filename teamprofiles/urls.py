# - *- coding: utf- 8 - *-

from django.conf.urls import url
from . import views

urlpatterns = [
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
]