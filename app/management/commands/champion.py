import requests
from django.core.management import BaseCommand
from app.models import Champion, ChampionTag


class Command(BaseCommand):
    def handle(self, *args, **options):
        site_pt_br = "https://ddragon.leagueoflegends.com/cdn/12.11.1/data/pt_BR/champion.json"
        site_en_us = "https://ddragon.leagueoflegends.com/cdn/12.11.1/data/en_US/champion.json"
        request = requests.get(site_pt_br).json()
        api_data = request["data"]

        self.get_champion_data(api_data, self.all_champions_name(api_data))

        self.get_champion_tags(api_data, self.all_champions_name(api_data))

    def all_champions_name(self, data):
        name_list = []
        for name in data:
            name_list.append(name)
        return name_list

    def get_champion_data(self, api_data, champion_keys):
        for champion_key in champion_keys:
            champion_api = api_data[champion_key]

            champion_name = champion_api["name"]
            title = champion_api["title"]
            description = champion_api["blurb"]

            champion_object = Champion.objects.filter(name=champion_name, title=title, description=description)

            if champion_object.exists():
                print(f"The champion: '{champion_name}' is already registered")
            else:
                Champion.objects.create(name=champion_name, title=title, description=description)

    def get_champion_tags(self, api_data, champion_keys):
        for champion_key in champion_keys:
            champion_api = api_data[champion_key]
            tags = champion_api["tags"]

            for tag in tags:
                tag_object = ChampionTag.objects.filter(name=tag)
                if tag_object.exists():
                    print(f"The tag: '{tag}' is already registered")
                else:
                    ChampionTag.objects.create(name=tag)


