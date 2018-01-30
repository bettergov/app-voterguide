from django.contrib import admin
from django.db import models
from django import forms

from .models import Election, Race, Candidate, Question, Response

# Register your models here.
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0
    formfield_overrides = {
        models.TextField: {
            'widget': forms.Textarea(
                attrs={'rows': 1, 'cols': 80}
            )
        }
    }

class CandidateInline(admin.TabularInline):
    model = Candidate
    extra = 0

class RaceAdmin(admin.ModelAdmin):
    inlines = [QuestionInline, CandidateInline]

class ResponseAdminForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ResponseAdminForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['question'].queryset = Question.objects.filter(race=self.instance.candidate.race)

class ResponseInline(admin.StackedInline):
    # form = ResponseAdminForm
    model = Response
    extra = 0

class CandidateAdmin(admin.ModelAdmin):
    inlines = [ResponseInline]

admin.site.register(Election)
admin.site.register(Race, RaceAdmin)
admin.site.register(Candidate, CandidateAdmin)
