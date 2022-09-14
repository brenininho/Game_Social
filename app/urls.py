from .views import dashboard, home
from django.urls import include, path
from rest_framework import routers
from .api.views import AccountViewSet, SummonerViewSet, MatchViewSet, MapViewSet, ParticipantViewSet, ChampionViewSet, \
    ItemViewSet, ItemTagViewSet
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()

router.register(r'account', AccountViewSet)
router.register(r'summoner', SummonerViewSet)
router.register(r'participant', ParticipantViewSet)
router.register(r'match', MatchViewSet)
router.register(r'map', MapViewSet)
router.register(r'champion', ChampionViewSet)
router.register(r'item', ItemViewSet)
router.register(r'item_tag', ItemTagViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
