from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import GolfCourse, Hole
from tournament.models import Tournament

# Create your views here.
def golf_course_list (request):
    golf_courses = get_list_or_404(GolfCourse.objects.all())
    context = {'golf_courses': golf_courses}
    return render(request, 'golf_course/golf_course_list.html', context)

def golf_course_detail(request, course_id):
    golf_course = get_object_or_404(GolfCourse, pk = course_id)
    holes = get_list_or_404(Hole, hole_course_id = course_id)
    tournaments = get_list_or_404(Tournament, tourn_course_id = course_id)
    context = {'tournaments': tournaments, 'golf_course': golf_course, 'holes': holes}
    return render(request,
                  'golf_course/golf_course_detail.html',
                  context)
