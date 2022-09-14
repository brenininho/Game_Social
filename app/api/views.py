from ..models import Account, Summoner, Match, Map, Participant, Champion, Item, ItemTag
from rest_framework import permissions, viewsets
from .serializers import AccountSerializer, SummonerSerializer, MatchSerializer, MapSerializer, ParticipantSerializer, \
    ChampionSerializer, ItemSerializer, ItemTagSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # permission_classes = [permissions.IsAuthenticated]


class SummonerViewSet(viewsets.ModelViewSet):
    queryset = Summoner.objects.all()
    serializer_class = SummonerSerializer
    # permission_classes = [permissions.IsAuthenticated]


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    # permission_classes = [permissions.IsAuthenticated]


class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ChampionViewSet(viewsets.ModelViewSet):
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ItemTagViewSet(viewsets.ModelViewSet):
    queryset = ItemTag.objects.all()
    serializer_class = ItemTagSerializer
    # permission_classes = [permissions.IsAuthenticated]
