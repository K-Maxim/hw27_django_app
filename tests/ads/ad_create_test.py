import pytest


@pytest.mark.django_db
def test_ad_create(client, user, category):
    expected_response = {
        'id': user.pk,
        'name': 'minimum of 10 characters',
        'author': user.pk,
        'price': 500,
        'description': 'test description',
        'is_published': False,
        'category': category.name,
        'image': None
    }

    data = {
        'name': 'minimum of 10 characters',
        'author': user.pk,
        'price': 500,
        'description': 'test description',
        'is_published': False,
        'category': category.id
    }

    response = client.post(
        '/ad/create/',
        data,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data == expected_response
