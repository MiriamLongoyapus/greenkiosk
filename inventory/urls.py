from django.urls import path 
from .views import product_upload

urlpatterns = [
    path("products/upload/", product_upload, name="product_upload"),
]