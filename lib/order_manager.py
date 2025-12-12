from lib.menu import *
from lib.order import *
from lib.receipt import *
from lib.sms_service import *

class OrderManager:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.menu = Menu()
        self.order = Order()
        self.receipt = Receipt()
        self.sms_service = SMSService()

    def show_menu(self):
        return self.menu.menu_list()
    
    def add_items(self, item, quantity=1):
        self.order.add_to_order(item, quantity)