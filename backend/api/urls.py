from django.urls import path
from api.views import create_item_view, retrieve_item_list_view

urlpatterns = [
    path("/create/item", create_item_view, name="create_item"),
    path("/items", retrieve_item_list_view, name="retrieve_items"),
]
