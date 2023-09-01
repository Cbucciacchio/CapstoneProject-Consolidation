import os
import django
from pokemontcgsdk import Set as TcgSet, Card as TcgCard

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PokemonCollector.settings')
django.setup()

from collection.views import populate_data

# Call the function directly since it doesn't need the request object
populate_data(None)
