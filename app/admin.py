from django.contrib import admin
from .models import Account, Summoner, Match, GameMode, Map, Participant, Champion, ChampionTag, Item, ItemTag


admin.site.register(Account)
admin.site.register(Summoner)
admin.site.register(Match)  # search widget manytomany
admin.site.register(GameMode)
admin.site.register(Map)
admin.site.register(Participant)
admin.site.register(Champion)
admin.site.register(ChampionTag)
admin.site.register(Item)
admin.site.register(ItemTag)
