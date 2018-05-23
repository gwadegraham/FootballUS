from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^Borussia Dortmund$', views.borussia_dortmund, name="borussia_dortmund"),
]