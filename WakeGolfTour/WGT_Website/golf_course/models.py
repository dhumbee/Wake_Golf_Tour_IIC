# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class GolfCourse(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_name = models.TextField()
    course_total_par = models.IntegerField()

    def getParList(self):
        hole_pars = []
        holes = Hole.objects.filter(
            hole_course_id =self.course_id)
        for hole in holes:
            hole_pars.append(hole.hole_par)
        return hole_pars

    def getGolferName(self):
        return self.tg_golfer.golfer_name

    def __str__(self):
        return self.course_name

    class Meta:
        managed = False
        db_table = 'GolfCourse'
        verbose_name = "Golf Course"
        verbose_name_plural = "Golf Courses"


class Hole(models.Model):
    hole_id = models.IntegerField(primary_key=True)
    hole_course = models.ForeignKey(GolfCourse, models.DO_NOTHING)
    hole_number = models.IntegerField()
    hole_par = models.IntegerField()

    def __str__(self):
        return "{}, Hole {}, Par {}".format(self.hole_course.course_name, self.hole_number, self.hole_par)

    class Meta:
        managed = False
        db_table = 'Hole'
