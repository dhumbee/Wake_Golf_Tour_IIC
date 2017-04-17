from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Golfer, GolferTournScores, TournGolfer, GolferRoundScores
from tournament.models import Tournament
from golf_course.models import GolfCourse, Hole

# Create your views here.
def golfer_list (request):
    golfers = get_list_or_404(Golfer.objects.all())
    context = {'golfers': golfers}
    return render(request, 'golfer/golfer_list.html', context)

def golfer_detail (request, golfer_id):
    golfer = get_object_or_404(Golfer, pk = golfer_id)
    scores = GolferTournScores.objects.filter(
        gts_tourn_golfer_id__tg_golfer = golfer_id)
    context = {'golfer': golfer, 'scores': scores}
    return render(request, 'golfer/golfer_detail.html', context)

def golfer_round_scores(request, tg_id):
    tourn_golfer = get_object_or_404(TournGolfer, pk = tg_id)
    tournament = get_object_or_404(Tournament, pk = tourn_golfer.tg_tourn.tourn_id)
    golf_course = get_object_or_404(GolfCourse, pk = tournament.tourn_course.course_id)
    holes = get_list_or_404(Hole, hole_course_id = golf_course.course_id)
    scores = GolferRoundScores.objects.filter(grs_tourn_golfer_id = tg_id)
    context = {'tourn_golfer': tourn_golfer, 'golf_course': golf_course, 'holes': holes, 'scores': scores}
    return render(request, 'golfer/golfer_round_scores.html', context)