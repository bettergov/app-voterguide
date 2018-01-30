from django.contrib import admin

from .models import Election, Race, Candidate

# Register your models here.
admin.site.register(Election)
admin.site.register(Race)
admin.site.register(Candidate)
