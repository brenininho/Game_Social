from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Account


@registry.register_document
class AccountDocument(Document):

    class Index:
        name = 'account'
        setting = {
            'number_of_shards': 1,
            'number_of_replicas': 1
        }

    class Django:
        model = Account

        fields = ["id",
                  "game_name",
                  "tag_line"
                  ]
