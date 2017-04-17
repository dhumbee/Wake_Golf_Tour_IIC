from django.contrib import admin
from .models import Golfer, TournGolfer, GolferRoundScores, GolferTournScores

class TournGolferAdmin(admin.ModelAdmin):
    list_display = ('tg_golfer', 'tg_tourn')
    list_filter = ['tg_tourn']
    search_fields = ['tg_golfer__golfer_name']
    exclude = ['tg_id']
    actions_on_top = False



class GolferTournScoresAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['gts_tourn_golfer']}),
                 ('Round scores', {'fields':
                ['gts_round1_score', 'gts_round2_score', 'gts_round3_score', 'gts_round4_score']}),
                 ('Total_score', {'fields': ['gts_total_score']})]
    list_display = ('golferName', 'tournName', 'gts_total_score')
    list_filter = ['gts_tourn_golfer__tg_tourn']
    ordering = ['gts_total_score']
    search_fields = ['gts_tourn_golfer__tg_golfer__golfer_name']
    exclude = ['gts_id']
    actions_on_top = False

    def tournName(self, gts):
        return gts.gts_tourn_golfer.tg_tourn.tourn_name

    tournName.short_description = 'Tournament'

    def golferName(self, gts):
        return gts.gts_tourn_golfer.tg_golfer.golfer_name
    golferName.short_description = 'Golfer'

class GolferRoundScoresAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['grs_tourn_golfer']}),
        (None, {'fields':[('grs_total_score', 'grs_round')]}),
        ('Scores(Front nine)', {'fields': [('grs_hole1_score', 'grs_hole2_score', 'grs_hole3_score',
                                           'grs_hole4_score', 'grs_hole5_score', 'grs_hole6_score',
                                           'grs_hole7_score', 'grs_hole8_score', 'grs_hole9_score',)]}),
        ('Scores(Back nine)', {'fields': [('grs_hole10_score', 'grs_hole11_score', 'grs_hole12_score',
                                           'grs_hole13_score', 'grs_hole14_score', 'grs_hole15_score',
                                           'grs_hole16_score', 'grs_hole17_score', 'grs_hole18_score',)]})
    ]
    list_display = ('golferName', 'tournName', 'grs_round', 'grs_total_score')
    list_filter = ['grs_tourn_golfer__tg_tourn__tourn_name']
    ordering = ['grs_round']
    search_fields = ['grs_tourn_golfer__tg_golfer__golfer_name']
    exclude = ['grs_id']
    actions_on_top = False

    def tournName(self, grs):
        return grs.grs_tourn_golfer.tg_tourn.tourn_name
    tournName.short_description = 'Tournament'

    def golferName(self, grs):
        return grs.grs_tourn_golfer.tg_golfer.golfer_name
    golferName.short_description = 'Golfer'

# Register your models here.
admin.site.register(TournGolfer, TournGolferAdmin)
admin.site.register(GolferRoundScores, GolferRoundScoresAdmin)
admin.site.register(GolferTournScores, GolferTournScoresAdmin)