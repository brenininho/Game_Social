from ..models import Account, Summoner, Match, Map, Participant, Champion, Item, ItemTag
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", 'game_name', 'tag_line']


class SummonerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Summoner
        fields = ["id", 'account', 'name', 'summoner_level']


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ["id", 'participant', 'game_mode', 'map', 'platform']


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ['name']


class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champion
        fields = ["id", 'name', 'title', 'description', 'image', 'price', 'sell']


class ItemTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTag
        fields = ["id", 'name']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", 'name', 'item_id']


class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = ["id", "summoner", 'kills', 'deaths', 'assists', 'champ_level', 'champion', 'lane', 'item',
                  'teamid', 'win']
