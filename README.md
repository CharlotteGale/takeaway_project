# Solo Project - Takeaway

## User Stories
> As a customer     
> So that I can check if I want to order something      
> I would like to see a list of dishes with prices.     

> As a customer     
> So that I can order the meal I want       
> I would like to be able to select some number of several available dishes.        

> As a customer     
> So that I can verify that my order is correct     
> I would like to see an itemised receipt with a grand total.       

> As a customer     
> So that I am reassured that my order will be delivered on time        
> I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.



## Class Interfaces
### Overlord: `OrderManager()`
```py
class OrderManager:
    pass
```

### `Menu()`
```py
class Menu:
    def __init__(self):
        # Internal State:
        #   self.menu_items = [] OR {}: empty list OR dictionary created on instantiation
        pass

    def menu_list(self):
        # Returns:
        #   A list of available items
        pass

```

### `Orders()`
```py
class Orders:
    def __init__(self, menu):
        # Parameters:
        #   instance of Menu
        # Internal State:
        #   self.order_items = [] OR {}: empty list OR dict created on instantiation
        pass

    def add_to_order(self, item, quantity=1):
        # Parameters:
        #   item: string
        #   quanitity: int defaulted to 1
        # Side Effects:
        #   adds item, price, and quantity to self.order_items
        pass
```

### `Receipts()`
```py
class Receipts:
    def __init__(self, order):
        # Parameters:
        #   instance of Order
        pass

    def generate_receipt(self):
        pass

    def __calculate_subtotals(self, quantity, price):
        # Parameters:
        #   orders.quantity: int
        #   orders.price: float
        # Side Effects:
        #   
        pass

    def __calculate_totals(self, subtotals_list):
        pass

    def __format_currency(self, price):
        pass
```

### `SMSService()`
```py
class SMSService:
    def send_sms_confirmation(self):
        pass

    def __call_sms_api(self):
        pass
```