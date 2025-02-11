from computer import *

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
        print(computer.description, "added to inventory")

        #1. to call Computer (...) constructor
        #   to create a new Computer instance

        #2. call inventory.append(....) to add the
        #   new Computer instance to the inventory

    def sell(self, computer:Computer):
        if computer is not None:
            self.inventory.pop(0) #remove computer from inventory
            print("Item", computer.description, "sold!")
        else:
            print("Item", computer.description, "not found. Please select another item to sell.") #if computer isn't in inventory

    
    def print_inventory(self):
        if self.inventory:
            for computer in self.inventory: #print all the computers in the inventory
                print(computer.description)
        else:
            print("No inventory to display.") #no inventory!
    
def main():
    
    # First, let's make a computer
    computer1 = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    shop = ResaleShop()

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    print("Buying", computer1.description)
    print("Adding to inventory...")
    shop.buy(computer1)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer1.description, ", updating OS to", new_OS)
    print("Updating inventory...")
    computer1.refurbish(new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer1.description)
    shop.sell(computer1)
    
    # Changing price of computer
    new_price = 1000
    print("Changing price of", computer1.description, "to $", new_price)
    computer1.update_price(new_price)
    print("The price is now", computer1.price, "\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

# Calls the main() function when this file is run
if __name__ == "__main__": 
    main()