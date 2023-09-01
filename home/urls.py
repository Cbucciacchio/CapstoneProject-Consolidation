from django.urls import path
from .views import home_view, default

urlpatterns = [
    path('home/', home_view, name='home'),
    path('', default, name='default'),

]