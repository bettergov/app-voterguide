from django.urls import path

from . import views

app_name = 'races'
urlpatterns = [
    # ex: /races/
    path('', views.index, name='index'),
    # ex: /races/1/
    path('<int:race_id>/', views.raceFromId, name="race"),
    # ex: /races/governor-dem
    path('<slug:race_slug>/', views.race, name="race")
]
