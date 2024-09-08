from django.urls import path, include
from api.views import (
    create_item_view,
    retrieve_item_list_view,
    retrieve_user_item_list_view,
    delete_item_view,
    retrieve_single_item_view,
    update_item_view,
)

urlpatterns = [
    path("/create/item", create_item_view, name="create_item"),
    path("/delete/<uuid:item_id>/item", delete_item_view, name="delete_item"),
    path(
        "/retrieve/<uuid:item_id>/item", retrieve_single_item_view, name="retrieve_item"
    ),
    path("/update/<uuid:item_id>/item", update_item_view, name="update_item"),
    path("/items", retrieve_item_list_view, name="retrieve_items"),
    path(
        "/retrieve/<pk:user_id>/items",
        retrieve_user_item_list_view,
        name="retrieve_user_items",
    ),
]
