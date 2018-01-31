from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Election, Race, Candidate, Question, Response

# Register your models here.

class RaceInline(admin.TabularInline):
    model = Race
    extra = 0
    show_change_link = True

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
    exclude = ('website', 'facebook', 'twitter', 'occupation', 'experience')
    show_change_link = True

class RaceAdmin(admin.ModelAdmin):
    inlines = (QuestionInline, CandidateInline)

    def has_delete_permission(self, request, obj=None): # note the obj=None
        return False

class ResponseInline(admin.StackedInline):
    model = Response
    extra = 0

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

    def get_form(self, request, obj=None, **kwargs):
        # just save obj reference for future processing in Inline
        request._obj_ = obj
        return super(CandidateAdmin, self).get_form(request, obj, **kwargs)

    def has_delete_permission(self, request, obj=None): # note the obj=None
        return False

admin.site.register(Election, ElectionAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(Candidate, CandidateAdmin)
