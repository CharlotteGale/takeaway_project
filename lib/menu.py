from lib.menu_data import MENU_ITEMS

class Menu:
    def __init__(self):
        self.menu_items = MENU_ITEMS
        
    def menu_list(self):
        return self.menu_items