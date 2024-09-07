from django.shortcuts import render
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
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
    model = Item
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ["item_type", "location_id", "status"]
    ordering_fields = ["location_id", "item_type"]

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
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
