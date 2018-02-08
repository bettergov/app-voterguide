from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Election, Race, Candidate

from webcolors import hex_to_rgb

colors = ["#b3e2cd","#fdcdac","#cbd5e8","#f4cae4","#e6f5c9","#fff2ae","#f1e2cc","#cccccc"]
colors = ["rgba" + str(hex_to_rgb(c) + (0.3,)) for c in colors]
election = get_object_or_404(Election, slug='2018-primary')
all_races = election.race_set.order_by('title')

def index(request):
    context = { 'all_races': all_races, 'title': "2018 Primary" }
    return render(request, 'qas/election.html', context)

def race(request, race_slug):
    race = get_object_or_404(Race, slug=race_slug)
    candidate_ids = request.GET.getlist('candidate[]')
    try:
        candidates = get_list_or_404(Candidate,pk__in=candidate_ids,race=race)
    except:
        candidates = None
    title = race.title
    context = { 'race': race, 'candidates': candidates, 'title': title, 'colors': colors, 'all_races': all_races }
    return render(request, 'qas/race.html', context)

def raceFromId(request, race_id):
    race = get_object_or_404(Race, pk=race_id)
    candidate_ids = request.GET.getlist('candidate[]')
    try:
        candidates = get_list_or_404(Candidate,pk__in=candidate_ids,race=race)
    except:
        candidates = race.candidate_set.all()
    title = race.title
    context = { 'race': race, 'candidates': candidates, 'title': title, 'colors': colors, 'all_races': all_races }
    return render(request, 'qas/race.html', context)

def faq(request):
    election = get_object_or_404(Election, pk=1)
    context = {'election': election,'title': "FAQ", 'all_races': all_races}
    return render(request, 'qas/faq.html', context)
