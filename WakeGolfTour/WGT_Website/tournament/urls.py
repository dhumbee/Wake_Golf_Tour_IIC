from django.conf.urls import url
from .views import tournament_list, tournament_detail

urlpatterns = [
    url(r'^tournament/$',
        tournament_list,
        name = 'tournament_list'),
    url(r'^(?P<tourn_id>[0-9]+)/$',
        tournament_detail,
        name='tournament_detail'),
]