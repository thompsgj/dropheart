import uuid

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Item(models.Model):
    ITEM_CHOICES = (
        ("ELECTRONICS", "Electronics"),
        ("BOOKS", "Books"),
        ("GAMES", "Games"),
        ("ARTS", "Arts"),
        ("MEN_FASHION", "Men_fashion"),
        ("WOMEN_FASHION", "Women_fashion"),
    )

    item_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        help_text="A unique ID associated with the item",
        editable=False,
    )
    location_id = models.TextField(help_text="Location ID associated with the item")
    item_type = models.CharField(
        choices=ITEM_CHOICES, max_length=15, help_text="Type of item dropped off"
    )
    image_path = models.TextField(
        help_text="Path to the image location in the cloud bucket"
    )
    list_time = models.DateTimeField(
        auto_now=True, help_text="The time that the item was listed"
    )
    status = models.CharField(
        max_length=15,
        choices=(("AVAILABLE", "Available"), ("UNAVAILABLE", "Unavailable")),
        help_text="The status of the item",
        default="AVAILABLE",
    )
    item_name = models.CharField(max_length=100, help_text="The name of the item")
    item_description = models.TextField(help_text="A description of the item")
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, help_text="The user id who dropped off the item"
    )

    def __str__(self):
        return self.item_name


# sort_api : location, category (AND/OR)
# search_api : product_name, location, status ()
