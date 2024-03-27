from django.urls import path, include, re_path
from . import api

urlpatterns = [
    path('drf-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('products/', api.ProductsListApi.as_view()),
    path('product/get/<int:pk>', api.ProductGetApi.as_view()),
    path('orders/list/', api.UserOrdersListApi.as_view()),
    path('orders/create/', api.OrderCreateApi.as_view()),
    path('order/<int:pk>', api.OrderApi.as_view()),
]
