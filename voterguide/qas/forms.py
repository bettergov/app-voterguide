from django import forms
from django.utils.text import slugify

from .models import Candidate, Race

class AddCandidate(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'

    def save(self, commit=True):
        instance = super(AddCandidate, self).save(commit=False)
        if not instance.id:
            instance.slug = slugify(instance.name)
        instance.save()

        return instance

class AddRace(forms.ModelForm):
    class Meta:
        model = Race
        fields = '__all__'

    def save(self, commit=True):
        instance = super(AddRace, self).save(commit=False)
        if not instance.id:
            instance.slug = slugify(instance.title)
        instance.save()

        return instance
