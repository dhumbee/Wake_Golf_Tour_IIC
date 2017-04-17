# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from tournament.models import Tournament, Round
from golf_course.models import GolfCourse
from django.db import models


class Golfer(models.Model):
    golfer_id = models.IntegerField(primary_key=True)
    golfer_name = models.TextField()

    def __str__(self):
        return self.golfer_name

    class Meta:
        managed = False
        db_table = 'Golfer'


class TournGolfer(models.Model):
    tg_id = models.IntegerField(primary_key=True)
    tg_tourn = models.ForeignKey(Tournament, models.DO_NOTHING)
    tg_golfer = models.ForeignKey(Golfer, models.DO_NOTHING)

    def getGolferName(self):
        return self.tg_golfer.golfer_name

    def getTournName(self):
        return self.tg_tourn.tourn_name

    def __str__(self):
        return "{} {}".format(self.tg_tourn.tourn_name, self.tg_golfer.golfer_name)

    class Meta:
        managed = False
        db_table = 'TournGolfer'
        verbose_name = "Tournament Golfer"
        verbose_name_plural = "Tournament Golfers"


class GolferRoundScores(models.Model):
    grs_id = models.IntegerField(primary_key=True)
    grs_tourn_golfer = models.ForeignKey(TournGolfer, models.DO_NOTHING)
    grs_round = models.ForeignKey(Round, models.DO_NOTHING)
    grs_total_score = models.IntegerField()
    grs_hole1_score = models.IntegerField()
    grs_hole2_score = models.IntegerField()
    grs_hole3_score = models.IntegerField()
    grs_hole4_score = models.IntegerField()
    grs_hole5_score = models.IntegerField()
    grs_hole6_score = models.IntegerField()
    grs_hole7_score = models.IntegerField()
    grs_hole8_score = models.IntegerField()
    grs_hole9_score = models.IntegerField()
    grs_hole10_score = models.IntegerField()
    grs_hole11_score = models.IntegerField()
    grs_hole12_score = models.IntegerField()
    grs_hole13_score = models.IntegerField()
    grs_hole14_score = models.IntegerField()
    grs_hole15_score = models.IntegerField()
    grs_hole16_score = models.IntegerField()
    grs_hole17_score = models.IntegerField()
    grs_hole18_score = models.IntegerField()

    def getParDiffs(self):
        scores = []
        for i in range(18):
            score = getattr(self, 'grs_hole{}_score'.format(i+1))
            scores.append(score)
        parList = self.grs_tourn_golfer.tg_tourn.tourn_course.getParList()
        print(parList)
        score_par_diff = []
        for i in range(18):
            score_par = []
            score_par.append(scores[i])
            difference = scores[i] - parList[i]
            score_par.append(difference)
            score_par_diff.append(score_par)
        return score_par_diff

    def __str__(self):
        return "{} {} {} {}".format(self.grs_tourn_golfer.tg_golfer, self.grs_tourn_golfer.tg_tourn, self.grs_round,
                                    self.grs_total_score)

    class Meta:
        managed = False
        db_table = 'GolferRoundScores'
        verbose_name = "Golfer Round Scores"
        verbose_name_plural = "Golfers Round Scores"


class GolferTournScores(models.Model):
    gts_id = models.IntegerField(primary_key=True)
    gts_tourn_golfer = models.ForeignKey(TournGolfer, models.DO_NOTHING)
    gts_total_score = models.IntegerField()
    gts_round1_score = models.IntegerField()
    gts_round2_score = models.IntegerField()
    gts_round3_score = models.IntegerField()
    gts_round4_score = models.IntegerField()

    def getGolferName(self):
        return self.gts_tourn_golfer.getGolferName()

    def getTournName(self):
        return self.gts_tourn_golfer.getTournName()

    def __str__(self):
        return "{} {}".format(self.gts_tourn_golfer, self.gts_total_score)

    class Meta:
        managed = False
        db_table = 'GolferTournScores'
        verbose_name = "Golfer Tournament Scores"
        verbose_name_plural = "Golfers Tournament Scores"
