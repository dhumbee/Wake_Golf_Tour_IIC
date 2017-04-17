from django.conf.urls import url
from .views import golf_course_list, golf_course_detail

urlpatterns = [
    url(r'^golf_course/$',
        golf_course_list,
        name = 'golf_course_list'),
    url(r'^(?P<course_id>[0-9]+)/$',
        golf_course_detail,
        name='golf_course_detail'),
]