from django.shortcuts import render

from .models import MainItem


def main_items(request):
    items = MainItem.objects.all()
    context = {
        'items': items
    }

    return render(request, 'main/items.html', context)
