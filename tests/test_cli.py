# tests/test_cli.py

from inventory import inventory


def test_inventory_exists():

    assert len(inventory) > 0


def test_inventory_item_structure():

    item = inventory[0]

    assert "id" in item
    assert "name" in item
    assert "brand" in item
    assert "price" in item
    assert "stock" in item
    assert "barcode" in item