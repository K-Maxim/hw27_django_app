import pytest


@pytest.mark.django_db
def test_ad_retrieve(client, ad, user_access):
    expected_response = {
        'id': ad.pk,
        'name': 'minimum of 10 characters',
        'author_id': ad.author_id.username,
        'price': 500,
        'description': None,
        'is_published': False,
        'category_id': ad.category_id.name,
        'image': None
    }

    response = client.get(
        f'/ad/{ad.pk}/',
        HTTP_AUTHORIZATION='Bearer ' + user_access
    )

    assert response.status_code == 200
    assert response.data == expected_response
