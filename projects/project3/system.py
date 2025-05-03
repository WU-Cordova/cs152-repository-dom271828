from projects.project3.drinks import Drink, OrderItem, CustomerOrder
from datastructures.array import Array
from datastructures.circularqueue import CircularQueue
from datastructures.linkedlist import LinkedList

class BistroSystem:

    def __init__(self, menu = list[Drink]):
        """ Attributes:
        menu - Hardcoded Array which stores a selection of Drink objects;
        confirmation - LinkedList of OrderItems to use when customer needs to confirm order;
        openqueue - CircularQueue which can store up to 10 full CustomerOrder objects;
        completed - LinkedList of CustomerOrder objects which have been completed, can be displayed;
        """
        self.menu: Array[Drink] = Array(starting_sequence=menu, data_type=Drink)
        self.confirmation: LinkedList[OrderItem] = LinkedList(data_type=OrderItem)
        self.openqueue: CircularQueue[CustomerOrder] = CircularQueue(maxsize=10, data_type=CustomerOrder)
        self.completed: LinkedList[CustomerOrder] = LinkedList(data_type=CustomerOrder)
        self.auto = False
    
    def display_menu(self):
        """Prints menu like such:
        1. London Fog - $4.50
        ..."""
        count = 1
        for drink in self.menu:
            print(f"{count}. {drink}")
            count += 1 # Count increases with display

    def take_new_order(self):
        """Command that:
        1. Asks for customer name, then creates a CustomerOrder with that name
        2. Prints the menu for reference
        3. Prompts user to pick the # of the drink they want
        4. Pulls this drink out of menu Array
        5. Prompts user for a customization, creates Orderitem based on that
        6. Adds order to CustomerOrder object and LinkedList Confirmation
        7. Prompts user to confirm order, adds to open orders"""
        currentname = input("What is your name? ").strip() # Twin peaks
        order = CustomerOrder(name=currentname)
        completed = False
        print("Here is the menu.")
        self.display_menu()
        while completed != True:
            ordernumber = input("Enter your drink you want according to its number. ").strip()
            currentdrink = self.menu[int(ordernumber) - 1]
            customization = input("Enter any customizations you may like: ").strip()
            currentorder = OrderItem(drink=currentdrink, customization=customization)
            order.add_order_item(currentorder)
            self.confirmation.append(currentorder)
            ok = input("Would you like another drink? (Y/N) ")
            if ok == "N":
                completed = True
        
        print()
        print("Here are your items:")
        for item in self.confirmation:
            print(item)
        
        self.confirmation.clear()
        print()
        valid = input("Please confirm if this is what you would like to order. ")

        if valid == "Y":
            self.openqueue.enqueue(order)
            if self.auto == True:
                self.mark_completed() # stealthily adds order to completed if auto is true

    
    def view_open_orders(self):
        """ Command that displays all open orders in queue, gives message if empty """
        if not self.openqueue.empty:
            print("Open Orders:")
            count = 0
            for order in self.openqueue.circularqueue:
                if order.name != None:
                    count += 1
                    order.display(count)
        elif self.auto == True:
            print("Automatic mode is on.") # If auto mode is on
        else:
            print("No open orders to display.") # If triggered with an empty queue
    
    def mark_completed(self):
        """ Command that dequeues first order in open orders queue and adds it to completed orders,
        first order is given priority """
        if not self.openqueue.empty:
            complete = self.openqueue.dequeue()
            self.completed.append(complete)
            if self.auto == False:
                print(f"Completed order for {complete.name}!")
        elif self.auto == True:
            print("Automatic mode is on.")
        else:
            print("No open orders to mark.")

    def end_of_day(self):
        """ Displays end of day report, with item, amount sold, and total revenue gained """
        totalrevenue = 0.00
        print("End of Day Report:")
        print()
        print("Item/ Qty/ Revenue")
        for item in self.menu:
            drinkrevenue = 0.00
            quantity = 0
            for drinkorder in self.completed:
                for drink in drinkorder.order:
                    if drink.drink == item:
                        quantity += 1
                        drinkrevenue += drink.drink.price # Adds revenue per particular drink
            totalrevenue += drinkrevenue # Adds revenue per any drink
            if quantity > 0:
                print(f"{item.item}/ {quantity}/ ${drinkrevenue}") # Compact
        print(f"Total Revenue: {totalrevenue}") 
    
    def run(self):
        """ Main program command, controls main menu and user interface by prompting users to input numbers 
        based on the action they would like to take """

        finished = False
        print("Welcome to the Bistro!!!")
        mode = input("Would you like to automatically mark orders as complete? (yes/no) ").strip().upper() # Maybe not the best setting for a busy coffee shop, but oh well
        if mode == "YES":
            self.auto = True
        print("1. Display Menu")
        print("2. Take New Order")
        print("3. View Open Orders")
        print("4. Mark Next Order as Complete")
        print("5. View End-Of-Day Report")
        print("6. Exit")
        print()
        while finished != True:

            user = input("Enter what you would like to do: ").strip()

            if user == "1": # Menu Display
                print()
                self.display_menu()
 
            if user == "2": # Order Input
                print()
                self.take_new_order()

            if user == "3": # Open order list
                print()
                self.view_open_orders()
            
            if user == "4": # Completion of order
                print()
                self.mark_completed()
            
            if user == "5": # End of Day Report
                print()
                self.end_of_day()
            
            if user == "6": # Quits program
                print("Goodbye!")
                finished = True
            
            if user != "6":
                print()
                print("Main Menu")
                user = None

        



        

            

