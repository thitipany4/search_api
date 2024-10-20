from django.contrib import admin
from django.urls import path
from myapi.views import *
from rest_framework import routers

urlpatterns = [
    path('',home),
    path('api/search/',ProductSearchAPI.as_view(),name='product_api')
]