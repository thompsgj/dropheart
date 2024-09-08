from django.shortcuts import render
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from api.models import Item
from api.serializers import ItemSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

class CreateItem(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
create_item_view = CreateItem.as_view()


class ReadItem(generics.ListAPIView):
    model = Item
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    filter_backends = [filters.OrderingFilter, SearchFilter]
    ordering_fields = ["location_id", "item_type"]
    search_fields = ["item_type", "location_id", "status"]

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)
retrieve_item_list_view = ReadItem.as_view()

class ReadUserItem(generics.ListAPIView):
    model = Item
    serializer_class = ItemSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        if user_id is None:
            raise ValidationError("user_id parameter is required")
        try:
            user_id = int(user_id)
        except ValueError:
            raise ValidationError("user_id must be an integer")
        return Item.objects.filter(user_id=user_id)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)

retrieve_user_item_list_view = ReadUserItem.as_view()

class DeleteItem(generics.DestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    lookup_field = "item_id"

    def delete(self, request, *args, **kwargs):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

delete_item_view = DeleteItem.as_view()

class RetrieveItem(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "item_id"

    def get(self, request, *args, **kwargs):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

retrieve_single_item_view = RetrieveItem.as_view()

class UpdateItem(generics.UpdateAPIView):
    serializer_class = ItemSerializer
    lookup_field = "item_id"

    def update(self, request, *args, **kwargs):
        item_id = self.kwargs.get("item_id")
        item = get_object_or_404(Item, item_id=item_id)
        serializer = self.get_serializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


update_item_view = UpdateItem.as_view()



