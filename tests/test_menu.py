from lib.menu import *
from lib.menu_data import MENU_ITEMS
import pytest

def test_menu_items_dict_created_on_init():
    # __init__
    menu = Menu()

    assert menu.menu_items == MENU_ITEMS

def test_menu_list_displays_menu_items():
    # menu_list
    menu = Menu()

    assert menu.menu_list() == menu.menu_items