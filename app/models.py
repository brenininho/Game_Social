from django.db import models
from rest_framework import serializers


def upload_image(instance, filename):
    return f"{instance.id}-{filename}"


class Account(models.Model):
    puuid = models.CharField(blank=True, max_length=40)  # by web scrapping
    game_name = models.CharField(max_length=40)
    tag_line = models.CharField(max_length=40, null=True, choices=[("BR1", "BR1"), ("NA", "NA"), ("EUW", "EUW")])

    def __str__(self):
        return "%s - #%s" % (self.game_name, self.tag_line)


class Summoner(models.Model):
    puuid = models.CharField(blank=True, max_length=40)  # by web scrapping
    account = models.ForeignKey(Account, blank=True, on_delete=models.PROTECT, null=True)
    name = models.CharField(blank=True, max_length=40, unique=True)
    profile_icon_id = models.CharField(blank=True, max_length=40)  # by web scrapping
    summoner_level = models.CharField(blank=True, max_length=10)

    def __str__(self):
        return "%s" % self.name


class Match(models.Model):
    participant = models.ManyToManyField("Participant", blank=True)
    game_mode = models.ForeignKey("GameMode", on_delete=models.SET_NULL, null=True)
    map = models.ForeignKey("Map", on_delete=models.SET_NULL, null=True)
    platform = models.CharField(max_length=40, null=True, choices=[("br1", "BR1"), ("na", "NA"), ("euw", "EUW")])

    # def save(self, *args, **kwargs):
    #     if self.participant.count() != 10:
    #         raise serializers.ValidationError("Choose 10 participants")
    #     return super(Match, self).save(*args, **kwargs)

    # def clean(self, *args, **kwargs):
    #     if self.participant is not None:
    #         if self.participant.count() > 10:
    #             raise serializers.ValidationError("Choose 10 participants, no more, no less")
    #
    # def save(self, *args, **kwargs):
    #     self.full_clean()
    #     return super().save(*args, **kwargs)


class GameMode(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "%s - #%s" % (self.name, self.description)


class Map(models.Model):
    id_map = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=40, blank=True, null=True)
    puuid = models.CharField(max_length=40, blank=True, null=True)  # não sei o que fazer ainda

    def __str__(self):
        return "%s - %s" % (self.name, self.description)


class Participant(models.Model):
    puuid = models.CharField(max_length=40)
    summoner = models.ForeignKey("Summoner", null=True, on_delete=models.SET_NULL)
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    champ_level = models.IntegerField()
    champion = models.ForeignKey("Champion", on_delete=models.SET_NULL, null=True)
    lane = models.CharField(blank=True, null=True, max_length=10, choices=[("top", "Top"), ("jungle", "Jungle"),
                                                                           ("middle", "Middle"), ("bottom", "Bottom")])
    item = models.ManyToManyField("Item", blank=True)
    teamid = models.CharField(max_length=4, choices=[("red", "Red"), ("blue", "Blue")])
    win = models.BooleanField("Venceu", default=False)

    def __str__(self):
        return "%s - %s - %s/%s/%s" % (self.summoner.name, self.champion.name, self.kills, self.deaths, self.assists)


class Champion(models.Model):
    name = models.CharField(max_length=40)
    champion_id = models.IntegerField(blank=True, null=True)  # by Webscrapping
    title = models.CharField(blank=True, max_length=40)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True, upload_to=upload_image)
    price = models.IntegerField(blank=True, null=True)
    sell = models.IntegerField(blank=True, null=True)
    tags = models.ManyToManyField("ChampionTag", blank=True)

    def __str__(self):
        return "%s - %s" % (self.name, self.title)

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()


class ChampionTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.name


class Item(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)
    plain_text = models.CharField(max_length=200, blank=True, null=True)
    item_id = models.IntegerField(null=True, blank=True)  #by WebScrapping

    def __str__(self):
        return "%s" % self.name


class ItemTag(models.Model):
    name = models.CharField(max_length=40, choices=[("manaregen", "ManaRegen"), ("healthregen", "HealthRegen")])  #implement tag choices

    def __str__(self):
        return "%s" % self.name




