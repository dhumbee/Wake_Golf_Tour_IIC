# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from golf_course.models import GolfCourse
from django.db import models


class Tournament(models.Model):
    tourn_id = models.IntegerField(primary_key=True)
    tourn_name = models.TextField()
    tourn_course = models.ForeignKey(GolfCourse, models.DO_NOTHING)
    tourn_start_date = models.TextField()
    tourn_num_rounds = models.IntegerField()
    tourn_num_golfers = models.IntegerField()

    def __str__(self):
        return self.tourn_name

    class Meta:
        managed = False
        db_table = 'Tournament'


class Round(models.Model):
    round_id = models.IntegerField(primary_key=True)
    round_tourn = models.ForeignKey(Tournament, models.DO_NOTHING)
    round_day = models.TextField()

    def __str__(self):
        return ("{}".format(self.round_day))

    class Meta:
        managed = False
        db_table = 'Round'


class TournScores(models.Model):
    ts_id = models.IntegerField(primary_key=True)
    ts_tourn = models.ForeignKey(Tournament, models.DO_NOTHING)
    ts_top_score = models.IntegerField()
    ts_top_round1_score = models.IntegerField()
    ts_top_round2_score = models.IntegerField()
    ts_top_round3_score = models.IntegerField()
    ts_top_round4_score = models.IntegerField()

    def __str__(self):
        return (" {} TopScore: {}".format(self.tr_tourn.tourn_name, self.tr_top_score))

    class Meta:
        managed = False
        db_table = 'TournScores'
        verbose_name = "Tournament Scores"
        verbose_name_plural = "Tournament Scores"
