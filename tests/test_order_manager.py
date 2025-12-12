from lib.order_manager import *
from lib.menu_data import MENU_ITEMS
from unittest.mock import Mock
import pytest

def test_phone_number_stored_on_init():
    # __init__
    """
    On init
    Ensure phone number stored as string
    """
    order_manager = OrderManager("07123456789")

    assert order_manager.phone_number == "07123456789"



# def test_internal_state_attributes_created_on_init_MOCK():
#     # __init
#     """
#     On init
#     Ensure self.menu and self.order created on instantiation
#     """
#     fake_menu = Mock()
#     fake_order = Mock()
#     fake_receipt = Mock()
#     fake_sms_service = Mock()
#     order_manager = OrderManager(
#         "07123456789",
#         menu=fake_menu,
#         order=fake_order,
#         receipt=fake_receipt,
#         sms_service=fake_sms_service
#         )

#     assert order_manager.menu == fake_menu
#     assert order_manager.order == fake_order
#     assert order_manager.receipt == fake_receipt
#     assert order_manager.sms_service == fake_sms_service

# def test_show_menu_from_menu_class_MOCK():
#     # show_menu
#     """
#     When OrderManager.show_menu is invoked
#     Return fake_menu_list
#     """
#     fake_menu = Mock()
#     fake_menu.menu_list.return_value = list(MENU_ITEMS.keys())
#     order_manager = OrderManager("07123456789", menu=fake_menu)

#     assert order_manager.show_menu() == fake_menu.menu_list

# def test_add_item_from_order_class_MOCK():
#     # add_item
#     """
#     Given an item and an optional quantity that defaults to one
#     Call MockOrder.add_to_order(item, quantity)
#     """
#     fake_order = Mock()
#     fake_order.add_to_order().order_items = {"Drunken Noodles": 2, "Massaman Curry": 2}

#     order_manager = OrderManager("07123456789", order=fake_order)

#     order_manager.add_items("Drunken Noodles", 2)
#     order_manager.add_items("Massaman Curry", 2)
    
#     assert order_manager.order == fake_order.add_to_order().order_items