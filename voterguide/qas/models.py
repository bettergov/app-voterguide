from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils.timezone import now


# Create your models here.
class Election(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, help_text="Automatically generated slug. Don't recommend changing!")
    date = models.DateField('election date')
    faq_text = RichTextField("FAQ text goes here", blank=True)

    def __str__(self):
        return self.title

class Race(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(help_text="Automatically generated slug. Don't recommend changing!")
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return  "%s: %s" % (self.election, self.title)

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(help_text="Automatically generated slug. Don't recommend changing!")
    time_added = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    is_incumbent = models.BooleanField()
    PARTY_CHOICES = (
        ('GOP', 'Republican'),
        ('DEM', 'Democrat')
    )
    special_status = models.CharField(max_length=255, blank=True)
    is_inactive = models.BooleanField(default=False)
    party = models.CharField(max_length=3, choices = PARTY_CHOICES)
    website = models.URLField(help_text="The url for the candidate's website.", blank=True)
    facebook = models.URLField(help_text="The url for the candidate's Facebook.", blank=True)
    twitter = models.URLField(help_text="The url for the candidate's Twitter.", blank=True)
    occupation = models.TextField(blank=True)
    experience = RichTextField("Elected offices held and civic involvement", blank=True)

    def __str__(self):
        return  "%s (%s)" % (self.name, self.race.election)

class Question(models.Model):
    question_text = models.TextField()
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self):
        question_text = self.question_text
        if len(question_text) > 50:
            question_text = question_text[:47] + "..."
        return question_text

class Response(models.Model):
    response_text = RichTextField()
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
