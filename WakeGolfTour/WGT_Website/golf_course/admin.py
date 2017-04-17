from django.contrib import admin
from .models import GolfCourse, Hole

class HoleInLine(admin.TabularInline):
    model = Hole
    max_num = 18
    can_delete = False
    exclude = ['hole_id']

class GolfCourseAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['course_name']})]
    inlines = [HoleInLine]
    exclude = ['course_id']
    actions_on_top = False
# Register your models here.
admin.site.register(GolfCourse, GolfCourseAdmin)