from django.conf.urls import url
from .views import golfer_list, golfer_detail, golfer_round_scores

urlpatterns = [
    url(r'^golfer/$',
        golfer_list,
        name = 'golfer_list'),
    url(r'^(?P<golfer_id>[0-9]+)/$',
        golfer_detail,
        name='golfer_detail'),
    url(r'^(?P<tg_id>[0-9]+)/round_scores/$',
        golfer_round_scores,
        name='golfer_round_scores'),
]