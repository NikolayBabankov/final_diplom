from django.shortcuts import render
from rest_framework.generics import ListAPIView
from shop.serializers import ShopSerializer
from shop.models import Shop


class ShopView(ListAPIView):
    """
    Класс для просмотра списка магазинов
    """
    queryset = Shop.objects.filter(state=True)
    serializer_class = ShopSerializer
