import requests
from django.core.management import BaseCommand
from app.models import GameMode


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        site = "https://static.developer.riotgames.com/docs/lol/gameModes.json"
        request = requests.get(site).json()
        self.get_mode(request)

    def get_mode(self, request):
        for mode in request:
            game_mode = mode["gameMode"]
            mode_description = mode["description"]

            mode_object = GameMode.objects.filter(name=game_mode, description=mode_description)
            if mode_object.exists():
                print(f"The map: '{game_mode}' - '{mode_description}' is already registered")
            else:
                GameMode.objects.create(name=game_mode, description=mode_description)
