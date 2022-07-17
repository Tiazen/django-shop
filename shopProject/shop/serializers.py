from rest_framework import serializers

from shop.models import ItemCategory, ShopCategory, ShopModel

class ShopCategorySerializer(serializers.ModelSerializer):
    """
    Serilizer to retrive and create Shop category with fields
    - name
    """

    class Meta:
        model = ShopCategory
        fields = ['id', 'name']


class ItemCategorySerializer(serializers.ModelSerializer):
    """
    Serializer to retrive and create Items Categories with fields
    - name
    """

    class Meta:
        model = ItemCategory
        fields = ['name']


class ShopCreateSerializer(serializers.ModelSerializer):  
    """
    Serializer to create shop.
    - name
    - description
    """

    class Meta:
        model = ShopModel
        fields = ['name', 'description', 'owner'] 


class ShopRetrieveSerializer(serializers.ModelSerializer):
    """
    Serializer to retrive shop.
    - name
    - desc
    - owner
    - categories
    """
    categories = ShopCategorySerializer(many=True)
    class Meta:
        model = ShopModel
        fields = ['name', 'description', 'owner', 'categories']


