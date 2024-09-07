import uuid

from django.db import models


class Item(models.Model):
    ITEM_CHOICES = (("SOCKS", "socks"), ("PADS", "pads"), ("UNDERWEAR", "underwear"))
    item_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        help_text="A unique ID associated with the item",
    )
    location_id = models.TextField(help_text="")
    item_type = models.CharField(
        choices=ITEM_CHOICES, help_text="Type of item dropped off", max_length=15
    )
    image_path = models.TextField(help_text="Path the image location in cloud bucket")
    # user_id = models.ForeignKey(help_text="The user id who dropped off the item")
    list_time = models.DateTimeField(
        auto_now=True, help_text="The time that the item was listed"
    )
