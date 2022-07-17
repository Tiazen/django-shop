import django
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from shop.models import ShopCategory, ShopModel
from shop.models import ItemCategory
from shop.serializers import ItemCategorySerializer, ShopCategorySerializer, ShopCreateSerializer, ShopRetrieveSerializer


class ShopCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ShopCategorySerializer
    queryset = ShopCategory.objects.filter(active=True)


class ItemCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ItemCategorySerializer
    queryset = ItemCategory.objects.all()


class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopRetrieveSerializer
    queryset = ShopModel.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = ShopCreateSerializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data)
        return Response(serializer.errors)

    @action(methods=['POST'], detail=True)
    def add_category(self, request, pk):
        shop: ShopModel = get_object_or_404(ShopModel, id=pk)
        categories = request.data.get('categories', [])
        for item in categories:
            try:
                category: ShopCategory = ShopCategory.objects.get(id=item)
                shop.categories.add(category)
            except ShopCategory.DoesNotExist:
                return Response("Not found", 404)
            except Exception as e:
                print(e) ## TODO add logging
                return Response("Something went wrong", 500)
        return Response("OK")
    
    @action(methods=['POST'], detail=True)
    def remove_category(self, request, pk):
        shop: ShopModel = get_object_or_404(ShopModel, id=pk)
        categories = request.data.get('categories', [])
        for item in categories:
            try:
                category: ShopCategory = ShopCategory.objects.get(id=item)
                shop.categories.remove(category)
            except ShopCategory.DoesNotExist:
                return Response("Not found", 404)
            except Exception as e:
                print(e) ## TODO add logging
                return Response("Something went wrong", 500)
        return Response("OK")