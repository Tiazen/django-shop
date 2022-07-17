
from email.mime import base
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shop import views

router = DefaultRouter()

router.register(r'shops/item_category', views.ItemCategoryViewSet)
router.register(r'shops/shop_category', views.ShopCategoryViewSet)
router.register(r'shops', views.ShopViewSet)
urlpatterns = [
    path('', include(router.urls)),
]