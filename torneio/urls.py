from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlayerViewSet, TournamentViewSet, MatchViewSet


router = DefaultRouter()
router.register(r'players', PlayerViewSet, basename='player')
router.register(r'tournaments', TournamentViewSet, basename='tournament')
router.register(r'matches', MatchViewSet, basename='match')

urlpatterns = [
    path('', include(router.urls)),
]