from lib.order import *
import pytest

def test_empty_dict_created_on_init():
    order = Order()

    assert order.order_items == {}

def test_add_to_order_adds_to_order_items():
    order = Order()

    order.add_to_order("Pad Thai", 2)

    assert order.order_items == {"Pad Thai": 2}

