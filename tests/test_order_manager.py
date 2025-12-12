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



