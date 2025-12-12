class Order:
    def __init__(self):
        self.order_items = {}

    def add_to_order(self, item, quantity):
        self.order_items[item] = quantity