from django.shortcuts import get_object_or_404, render

from .models import Race, Candidate

def index(request):
    all_races = Race.objects.order_by('title')
    context = { 'all_races': all_races }
    return render(request, 'qas/index.html', context)

def race(request, race_id):
    race = get_object_or_404(Race, pk=race_id)
    return render(request, 'qas/race.html', { 'race': race })
