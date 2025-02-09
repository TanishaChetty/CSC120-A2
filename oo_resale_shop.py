from computer import *

class ResaleShop:

    # What attributes will it need?
    item_id: int
    inventory = []


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, item_id):
        pass # You'll remove this when you fill out your constructor

    # What methods will you need?
    def buy(self, computer: Computer):
        self.inventory.append(computer)
        print("Computer", self.item_id, "added to inventory")

        #1. to call Computer (...) constructor
        #   to create a new Computer instance

        #2. call inventory.append(....) to add the
        #   new Computer instance to the inventory

    def sell(self, computer:Computer):
        if self.item_id is not None:
            self.inventory.pop(computer)
            print("Item", self.item_id, "sold out!")
        else:
            print("Item", self.item_id, "not found. Please select another item to sell.")

    def refurbish(self, item_id: int, new_os:str):
        if:
        else:
    
    def print_inventory(self,self.inventory:list):
        if self.inventory:
            print("")
        else: