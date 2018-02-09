from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Election, Race, Candidate, Question, Response
from .forms import AddCandidate, AddRace

# Register your models here.

class RaceInline(admin.TabularInline):
    model = Race
    extra = 0
    show_change_link = True
    form = AddRace
    ordering = ('weight','title',)
    exclude = ('slug',)

class ElectionAdmin(admin.ModelAdmin):
    inlines = (RaceInline,)

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0
    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(
                attrs={'rows': 1, 'cols': 80}
            )
        }
    }

class CandidateInline(admin.TabularInline):
    model = Candidate
    extra = 0
    fields = ('name', 'is_incumbent', 'party')
    ordering = ('name',)
    show_change_link = True
    form = AddCandidate

class RaceAdmin(admin.ModelAdmin):
    inlines = (QuestionInline, CandidateInline)
    form = AddRace
    list_display = ('title', 'election', 'get_candidates', 'get_questions')
    list_filter = ['election']

    def get_questions(self, obj):
        questions = obj.question_set.all()
        return len(questions)
    get_questions.short_description = 'Questions'

    def get_candidates(self, obj):
        candidates = obj.candidate_set.all()
        return len(candidates)
    get_candidates.short_description = 'Candidates'

class ResponseInline(admin.StackedInline):
    model = Response
    extra = 0
    fields = ('question', 'response_text')
    ordering = ('question__question_text',)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):

        field = super(ResponseInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == 'question':
            if request._obj_ is not None:
                field.queryset = field.queryset.filter(race__exact = request._obj_.race)  
            else:
                field.queryset = field.queryset.none()

        return field

class CandidateAdmin(admin.ModelAdmin):
    inlines = (ResponseInline,)
    form = AddCandidate

    def get_form(self, request, obj=None, **kwargs):
        # just save obj reference for future processing in Inline
        request._obj_ = obj
        return super(CandidateAdmin, self).get_form(request, obj, **kwargs)
    
    list_display = ('name', 'get_race', 'get_election', 'get_responses', 'time_updated')
    list_filter = ['race']
    ordering = ('-time_updated',)

    def get_race(self, obj):
        return obj.race.title
    get_race.admin_order_field  = 'race' # Allows column order sorting
    get_race.short_description = "Race" # Rename column head

    def get_election(self, obj):
        return obj.race.election.title
    get_election.short_description = "Election" # Rename column head

    def get_responses(self, obj):
        responses = obj.response_set.all()
        questions = obj.race.question_set.all()
        return "%s/%s" % (len(responses), len(questions))
    get_responses.short_description = 'Responses'

admin.site.register(Election, ElectionAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(Candidate, CandidateAdmin)
