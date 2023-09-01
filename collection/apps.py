from django.apps import AppConfig
from pokemontcgsdk import RestClient

class CollectionConfig(AppConfig):
    name = 'collection'

    def ready(self):
        RestClient.configure('620a6087-241e-4985-b864-7377c3bdacde')
