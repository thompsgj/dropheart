from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from api.models import Item
from api.serializers import ItemSerializer

# Create your views here.


# Create
class CreateItem(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = [IsAdminUser]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)


create_item_view = CreateItem.as_view()


class ReadItem(generics.ListAPIView):
    model = Item
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)


retrieve_item_list_view = ReadItem.as_view()

# Delete


# Update
