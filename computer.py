class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str, 
                 processor_type: str, 
                 hard_drive_capacity: int, 
                 memory: int, 
                 operating_system: str, 
                 year_made: int, 
                 price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
         # You'll remove this when you fill out your constructor

    # What methods will you need?
    def update_price(self, new_price:int):
            self.price = new_price #updates price to new price
            print("The new price of this computer is", self.price)

    def update_os(self, new_os:str):
        self.operating_system = new_os #updates os to new os
        print("Updating OS to", self.operating_system)

    def refurbish(self, new_os:str): 
        if self.year_made < 2000 :
            self.price = 0 
        elif self.year_made < 2012:
            self.price = 250
        elif self.year_made < 2018:
            self.price = 550
        else:
            self.price = 1000 
            print("Computer Refurbished. New price is", self.price)
            #changes price based on what year it was made

        if new_os is not None:
            self.operating_system = new_os
            print("OS is now", new_os)
            #changes os to new one


