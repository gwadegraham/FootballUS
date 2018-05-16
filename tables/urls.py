# from django.conf.urls import url

# from . import views

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^$/bundesliga_1', views.bundesliga_1, name='bundesliga_1'),
# ]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # soccer league tables
    url(r'^bundesliga_1$', views.bundesliga_1, name="bundesliga_1"),
    url(r'^premier_league$', views.premier_league, name="premier_league"),
    url(r'^ligue_one$', views.ligue_one, name="ligue_one"),
    url(r'^serie_a$', views.serie_a, name="serie_a"),
    url(r'^laliga$', views.laliga, name="laliga") 
]