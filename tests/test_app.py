# tests/test_app.py

from app import app


def test_get_inventory():

    client = app.test_client()

    response = client.get("/inventory")

    assert response.status_code == 200


def test_get_single_item():

    client = app.test_client()

    response = client.get("/inventory/1")

    assert response.status_code == 200


def test_item_not_found():

    client = app.test_client()

    response = client.get("/inventory/999")

    assert response.status_code == 404


def test_search_openfoodfacts():

    client = app.test_client()

    response = client.get("/inventory/search/3017620422003")

    assert response.status_code == 200


def test_search_inventory():

    client = app.test_client()

    response = client.get("/inventory/search-name/milk")

    assert response.status_code == 200