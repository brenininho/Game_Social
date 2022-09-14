from django.urls import include, path
from rest_framework import routers
from .views import AccountViewSet, SummonerViewSet, MatchViewSet, MapViewSet, ParticipantViewSet, ChampionViewSet, \
    ItemViewSet, ItemTagViewSet

router = routers.DefaultRouter()

# router.register(r'users', AccountViewSet)
# router.register(r'users', SummonerViewSet)
# router.register(r'users', MatchViewSet)
# router.register(r'users', MapViewSet)
# router.register(r'users', ParticipantViewSet)

urlpatterns = [
    # path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
