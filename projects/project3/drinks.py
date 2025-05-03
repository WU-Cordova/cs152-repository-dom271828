from datastructures.array import Array
from datastructures.linkedlist import LinkedList

class Drink:
    def __init__(self, item: str, price: float):
        """Attributes:
        item - drink name;
        price - drink price;
        size - drink size (Defaults to medium)

        Usually Hardcoded from menu array."""
        self._item = item
        self._price = price
        self._size = "Medium"

    @property
    def price(self):
        """ Price property """
        return self._price
    
    @property
    def item(self):
        """ Item propeerty """
        return self._item
    
    @property
    def size(self):
        """ Size Property """
        return self._size
    
    def __str__(self):
        """Returns a string representation of the drink"""
        return(f"{self._item} - ${self._price}")
    
class OrderItem:
    def __init__(self, drink: Drink, customization: str):
        """ Attributes:
        drink - drink: Drink;
        custom - customization as added by the customer """
        self._drink = drink
        self._custom = customization

    @property
    def drink(self):
        return self._drink
    
    @property
    def customization(self):
        return self._custom
    
    def __str__(self):
        return f"{self._drink.item} ({self._drink.size}) with {self.customization}"
    
class CustomerOrder:
    def __init__(self, name = None):
        """ Attributes:
        name - name of customer: str (defaults to none, for usage in circular queue);
        order - array of OrderItems"""
        self._name = name
        self._order : LinkedList = LinkedList(data_type=OrderItem)
    
    def add_order_item(self, item: OrderItem) -> None:
        """ Appends order to order linkedlist """
        self._order.append(item)

    @property
    def name(self):
        return self._name

    @property 
    def order(self):
        return self._order
      
    @name.setter
    def name(self, name):
        self._name = name

    def display(self, count):
        """ Displays order
        Example: 
        1. John: Mocha (Oatmilk, Espresso), London Fog (Extra Hot)"""
        print(f"{count}. {self.name}: {", ".join([i.__str__() for i in self.order])}")
    
    
