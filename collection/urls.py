from django.urls import path
from . import views
from .views import cards_view

urlpatterns = [
    path('collection/', views.collection_view, name='collection'),
    path('collection/<str:set_id>/', views.cards_view, name='cards'),
    path('cards/<str:set_id>/', cards_view, name='cards_view_with_id'),
    path('cards/', cards_view, name='cards_view_without_id'),
    path('my_collection/', views.my_collection, name='my_collection'),
    path('add_card_to_collection/<str:id>/', views.add_card_to_collection, name='add_card_to_collection'),
    path('remove_card_from_collection/<str:id>/', views.remove_card_from_collection, name='remove_card_from_collection'),
    path('populate_data/', views.populate_data, name='populate_data'),
]

