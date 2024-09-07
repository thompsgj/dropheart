from django.shortcuts import render
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from api.models import Item
from api.serializers import ItemSerializer
from rest_framework import status


class CreateItem(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)


create_item_view = CreateItem.as_view()


class ReadItem(generics.ListAPIView):
    # sort_api : location, category (AND/OR)
    model = Item
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    filter_backends = [filters.OrderingFilter, SearchFilter]
    ordering_fields = ["location_id", "item_type"]
    # search_api : product_name, location, status ()
    search_fields = ["item_type", "location_id", "status"]

    def get(self, request):
        queryset = self.get_queryset()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)


retrieve_item_list_view = ReadItem.as_view()


class DeleteItem(generics.DestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    lookup_field = "item_id"


delete_item_view = DeleteItem.as_view()


class RetrieveItem(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "item_id"


retrieve_single_item_view = RetrieveItem.as_view()


class UpdateItem(generics.UpdateAPIView):
    serializer_class = ItemSerializer
    lookup_field = "item_id"

    def update(self, request, *args, **kwargs):
        item_id = self.kwargs.get("item_id")
        queryset = Item.objects.filter(item_id=item_id).update(**request.data)
        return Response(queryset)


update_item_view = UpdateItem.as_view()


from django.contrib.auth.models import User

first_names = ["James", "Jakob", "Min", "Bob", "Dragon"]
last_names = ["Brooklyn", "Grazy", "Corn", "Fragment", "Graze"]


import random


def create_users():
    for i in range(5):
        username = f"{random.choice(first_names)}_{random.choice(last_names)}"
        password = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=8))
        user = User.objects.create_user(username=username, password=password)
        user.save()
        print(f"User {user.username} created successfully.")


class UserList(generics.ListAPIView):
    # sort_api : location, category (AND/OR)
    model = User

    def get(self, request):
        create_users()

        queryset = User.objects.all()
        return Response(queryset)


retrieve_user_list_view = UserList.as_view()
