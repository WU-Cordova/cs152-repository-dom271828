from projects.project3.drinks import Drink, OrderItem, CustomerOrder
from projects.project3.system import BistroSystem

def main():
    menu = [Drink(item="London Fog", price=4.50), Drink(item="Mocha", price=4.50), Drink(item="Chai", price=5.00), Drink(item="Red Bull", price=3.50), Drink(item="Steamer", price=3.000)]
    system = BistroSystem(menu=menu)
    system.run()
    



if __name__ == '__main__':
    main()
