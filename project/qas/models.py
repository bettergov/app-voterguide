from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Election(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    date = models.DateField('election date')

    def __str__(self):
        return self.title

class Race(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    election = models.ForeignKey(Election, on_delete=models.CASCADE)

    def __str__(self):
        return  "%s (%s)" % (self.title, self.election)

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    is_incumbent = models.BooleanField()
    PARTY_CHOICES = (
        ('GOP', 'Republican'),
        ('DEM', 'Democrat')
    )
    party = models.CharField(max_length=3, choices = PARTY_CHOICES)
    website = models.URLField(help_text="The url for the candidate's website.", blank=True)
    facebook = models.URLField(help_text="The url for the candidate's Facebook.", blank=True)
    twitter = models.URLField(help_text="The url for the candidate's Twitter.", blank=True)
    # responses = ArrayField( Response() )

    def __str__(self):
        return  "%s (%s)" % (self.name, self.race.election)

class Question(models.Model):
    question_text = models.TextField()
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self):
        return "%s: %s" % (self.race, self.question_text)

class Response(models.Model):
    response_text = models.TextField()
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
