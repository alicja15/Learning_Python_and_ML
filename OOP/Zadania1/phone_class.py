

class Phone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    def call(self):
        if self.battery > 0:
            print("Calling...")
        else: #else czy if battery == 0?
            print("Battery empty")
            

phone1 = Phone("Samsung", "S24", 2) #nie dziala dla 2%
phone1.call() 
