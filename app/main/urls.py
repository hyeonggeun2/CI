from django.urls import path

from .views import main_items

app_name = 'main'

urlpatterns = [
    path('items/', main_items, name='main_items')
]