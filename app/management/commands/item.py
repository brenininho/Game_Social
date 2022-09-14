import requests
from django.core.management import BaseCommand
from app.models import Item, ItemTag
from bs4 import BeautifulSoup


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        site_pt_br = "https://ddragon.leagueoflegends.com/cdn/12.11.1/data/pt_BR/item.json"
        site_en_us = "https://ddragon.leagueoflegends.com/cdn/12.11.1/data/en_US/item.json"
        request = requests.get(site_pt_br).json()

        self.get_item(request["data"], self.all_item_key(request["data"]))

        self.get_item_tag(request["data"], self.all_item_key(request["data"]))

    def all_item_key(self, data):
        key_list = []
        for key in data:
            key_list.append(key)
        return key_list

    def get_item(self, api_data, key):
        for item_key in key:
            item_api = api_data[item_key]

            item_id = item_key

            name_api = item_api["name"]
            name = BeautifulSoup(name_api, "lxml").text

            description_api = item_api["description"]
            description = BeautifulSoup(description_api, "lxml").text

            plain_text_api = item_api["plaintext"]
            plain_text = BeautifulSoup(plain_text_api, "lxml").text

            item_object = Item.objects.filter(
                name=name,
                description=description,
                plain_text=plain_text,
                item_id=item_id
            )

            if item_object.exists():
                print(f"The item: {name} is already registered")
            else:
                Item.objects.create(name=name, description=description, plain_text=plain_text, item_id=item_id)

    def get_item_tag(self, api_data, key):

        for item_key in key:
            item_api = api_data[item_key]

            tags = item_api["tags"]

            for tag in tags:
                tag_object = ItemTag.objects.filter(name=tag)

                if tag_object.exists():
                    print(f"The item tag: {tag} is already registered")
                else:
                    ItemTag.objects.create(name=tag)
