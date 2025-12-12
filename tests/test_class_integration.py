from lib.order_manager import *
from lib.menu import *
from lib.order import *
from lib.receipt import *
from lib.sms_service import *
import pytest

def test_internal_state_attributes_created_on_init():
    # __init__
    """
    On init
    Ensure instance variables created on instantiation
    """
    order_manager = OrderManager("07123456789")

    assert isinstance(order_manager.menu, Menu)
    assert isinstance(order_manager.order, Order)
    assert isinstance(order_manager.receipt, Receipt)
    assert isinstance(order_manager.sms_service, SMSService)

def test_show_menu_from_menu_class():
    # show_menu
    """
    When OrderManager.show_menu is invoked
    Return Menu.menu_list
    """
    order_manager = OrderManager("07123456789")
    menu = Menu()

    assert order_manager.show_menu() == menu.menu_list()

def test_add_item_from_order_class():
    # add_item
    """
    Given an item and an optional quantity that defaults to one
    Call Order.add_to_order(item, quantity)
    """
    order_manager = OrderManager("07123456789")

    order_manager.add_items("Pad Thai", 2)

    assert "Pad Thai" in order_manager.order.order_items

# def test_show_receipt_from_receipt_class():
#     # show_receipt
#     """
#     When 
#     """