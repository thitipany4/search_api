from django.contrib import admin
from django.urls import path
from myapi.views import *
from rest_framework import routers

urlpatterns = [
    path('',home,name='home'),
    path('search/',send_api,name='send_api'),
    path('api/products/',ProductView.as_view(),name='product_api_view'),
    path('api/search/',ProductSearchAPI.as_view(),name='product_api_search'),


]