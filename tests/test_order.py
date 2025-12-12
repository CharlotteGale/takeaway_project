from lib.order import *
import pytest

def test_empty_dict_created_on_init():
    # __init__
    """
    On initialisation
    Ensure order_items is an empty dictionary
    """
    order = Order()

    assert order.order_items == {}

def test_add_to_order_adds_to_order_items():
    # add_to_order
    """
    When called with an item and a quantity
    Ensure the params are added to order_items
    """
    order = Order()

    order.add_to_order("Pad Thai", 2)

    assert order.order_items == {"Pad Thai": 2}

