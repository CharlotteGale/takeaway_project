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
    def __init__(self, phone_number, sms_service=None):
        # Parameters:
        #   phone_number: string (e.g. "07123456789")
        #   sms_service=None: optional instance of SMSService
        # Internal State:
        #   self.phone_number: stores the phone number
        #   self.menu: instance of Menu()
        #   self.order: instance of Order()
        #   self.sms_service: instance of SMSService() or injected mock
        pass

    def show_menu(self):
        # Returns:
        #   Menu.menu_list
        pass

    def add_item(self, item, quantity=1):
        # Parameters:
        #   item: string
        #   quantity: int (default 1)
        # Side Effects:
        #   calls Order.add_to_order(item, quantity)
        pass
    
    def show_receipt(self):
        # Returns:
        #   Receipt.generate_receipt
        pass

    def place_order(self):
        # Side Effects:
        #   calls SMSService.send_sms_confirmation() with phone number and message
        pass
```

### `Menu()`
```py
class Menu:
    def __init__(self):
        # Internal State:
        #   self.menu_items = {}: empty dict created on instantiation
        pass

    def menu_list(self):
        # Returns:
        #   A list of available items
        pass

```

### `Order()`
```py
class Order:
    def __init__(self, menu):
        # Parameters:
        #   instance of Menu
        # Internal State:
        #   self.order_items = []: empty list created on instantiation
        pass

    def add_to_order(self, item, quantity):
        # Parameters:
        #   item: string
        #   quanitity: int
        # Side Effects:
        #   adds item, price, and quantity to self.order_items
        pass
```

### `Receipt()`
```py
class Receipt:
    def __init__(self, order):
        # Parameters:
        #   instance of Order
        pass

    def generate_receipt(self):
        # Returns:
        #   a list showing an itemised receipt, with item and formatted currency
        #   and the grand total.
        pass

    def __calculate_subtotals(self):
        # Returns:
        #   a dictionary after looping through self.order
        pass

    def __calculate_totals(self, subtotals):
        # Parameters:
        #   subtotals: dictionary (from __calculate_subtotals)
        # Returns:
        #   adds all subtotals together and returns a float
        pass

    def __format_currency(self, grand_total):
        # Parameters:
        #   grand_total: float
        # Returns:
        #   string formatted as '£0.00'
        pass
```

### `SMSService()`
```py
class SMSService:
    def __init__(self, api_key=None):
        # Parameters:
        #   api_key: string, optional (defaults to env variable or config)
        # Internal State:
        #   self.api_key: stored API key for SMS service
        #   self.api_url: SMS service endpoint URL
        pass

    def send_confirmation(self, phone_number, message):
        # Parameters:
        #   phone_number: string (e.g. "07123456789")
        #   message: string (the confirmation text)
        # Side Effects:
        #   calls __call_sms_api to send SMS
        # Returns:
        #   boolean: True if successful, False if failed
        pass

    def __call_sms_api(self, phone_number, message):
        # Parameters:
        #   phone_number: string 
        #   message: string
        # Side Effects:
        #   Makes HTTP POST request to SMS API
        #   Sends an actual SMS
        # Returns:
        #   API response object or error
        # Notes:
        #   This method will be mocked in tests
        pass
```

## Test Examples
```py
    # __init__
    """
    On init
    Ensure phone number stored as string
    """
    order_manager = OrderManager("07123456789")

    assert order_manager.phone_number == "07123456789"
```

```py 
    # __init
    """
    On init
    Ensure self.menu and self.order created on instantiation
    """
    fake_menu = Mock()
    fake_order = Mock()
    fake_receipt = Mock()
    fake_sms_service = Mock()
    order_manager = OrderManager(
        "07123456789",
        menu=fake_menu,
        order=fake_order,
        receipt=fake_receipt,
        sms_service=fake_sms_service
        )

    assert order_manager.menu == fake_menu
    assert order_manager.order == fake_order
    assert order_manager.receipt == fake_receipt
    assert order_manager.sms_service == fake_sms_service
```

```py
    # show_menu
    """
    When OrderManager.show_menu is invoked
    Return fake_menu_list
    """
    fake_menu = Mock()
    fake_menu.menu_list.return_value = list(MENU_ITEMS.keys())
    order_manager = OrderManager("07123456789", menu=fake_menu)

    assert order_manager.show_menu() == fake_menu.menu_list
```

```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
```py

```
