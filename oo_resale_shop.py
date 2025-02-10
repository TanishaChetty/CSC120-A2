from computer import *
from procedural_resale_shop import buy, print_inventory, refurbish, sell

class ResaleShop:

    # What attributes will it need?
    inventory = []


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
         inventory = []
         # You'll remove this when you fill out your constructor

    # What methods will you need?
    def buy(self, computer: Computer):
        self.inventory.append(computer) #add computer to inventory
        print(computer, "added to inventory")

        #1. to call Computer (...) constructor
        #   to create a new Computer instance

        #2. call inventory.append(....) to add the
        #   new Computer instance to the inventory

    def sell(self, computer:Computer):
        if computer is not None:
            self.inventory.pop(computer) #remove computer from inventory
            print("Item", computer, "sold!")
        else:
            print("Item", computer, "not found. Please select another item to sell.") #if computer isn't in inventory

    
    def print_inventory(self):
        if self.inventory:
            for computer in self.inventory: #print all the computers in the inventory
                print(computer)
        else:
            print("No inventory to display.") #no inventory!
    
def main():
   # buy({'description': '2019 MacBook Pro', 'processor_type': 'Intel', 'hard_drive_capacity': 256, 'memory': 16, 'operating_system': 'High Sierra', 'year_made': 2019, 'price': 1000})
    refurbish(0, "OS Monterey")
    print_inventory()

main()