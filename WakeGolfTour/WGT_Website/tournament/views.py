from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Tournament
from golfer.models import GolferTournScores


# Create your views here

def tournament_list(request):
    tournaments = get_list_or_404(Tournament.objects.all())
    context = {'tournaments': tournaments}
    return render(request, 'tournament/tournament_list.html', context)

def tournament_detail(request, tourn_id):
    tournament = get_object_or_404(Tournament, pk = tourn_id)
    scores = GolferTournScores.objects.filter(
        gts_tourn_golfer_id__tg_tourn = tourn_id).order_by('gts_total_score')
    context = {'tournament': tournament, 'scores': scores}
    return render(request,
                  'tournament/tournament_detail.html',
                  context)