from django.test import TestCase
import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from api.models import Item
from api.serializers import ItemSerializer

@pytest.mark.django_db
def test_create_item():
    client = APIClient()
    url = reverse('create_item')  # Update with the correct URL name if needed
    data = {
        'item_id': 1,
        'item_type': 'example',
        'location_id': 123,
        'status': 'available',
        'user_id': 1
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Item.objects.count() == 1
    assert Item.objects.get().item_id == 1

@pytest.mark.django_db
def test_read_item_list():
    Item.objects.create(item_id=1, item_type='example', location_id=123, status='available', user_id=1)
    client = APIClient()
    url = reverse('retrieve_item_list')  # Update with the correct URL name if needed
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

@pytest.mark.django_db
def test_read_user_item_list():
    Item.objects.create(item_id=1, item_type='example', location_id=123, status='available', user_id=1)
    client = APIClient()
    url = reverse('retrieve_user_item_list') + '?user_id=1'  # Update with the correct URL name if needed
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

@pytest.mark.django_db
def test_delete_item():
    item = Item.objects.create(item_id=1, item_type='example', location_id=123, status='available', user_id=1)
    client = APIClient()
    url = reverse('delete_item', kwargs={'item_id': item.item_id})  # Update with the correct URL name if needed
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Item.objects.count() == 0

@pytest.mark.django_db
def test_retrieve_single_item():
    Item.objects.create(item_id=1, item_type='example', location_id=123, status='available', user_id=1)
    client = APIClient()
    url = reverse('retrieve_single_item', kwargs={'item_id': 1})  # Update with the correct URL name if needed
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['item_id'] == 1

@pytest.mark.django_db
def test_update_item():
    item = Item.objects.create(item_id=1, item_type='example', location_id=123, status='available', user_id=1)
    client = APIClient()
    url = reverse('update_item', kwargs={'item_id': item.item_id})  # Update with the correct URL name if needed
    data = {
        'item_type': 'updated_example'
    }
    response = client.patch(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    item.refresh_from_db()
    assert item.item_type == 'updated_example'


# Create your tests here.
