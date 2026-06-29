class Vehicle:
    def __init__(self, brand, model, max_speed):
        self.brand = brand
        self.model = model
        self._max_speed = max_speed
        
    def describe(self):
        print("\nVehicle details:")
        print(f"  Brand: {self.brand}\n  Model: {self.model}\n  Max Speed: {self._max_speed}")
    
class Car(Vehicle):
    def __init__(self, brand, model, max_speed, fuel_type):
        super().__init__(brand, model, max_speed)
        self.fuel_type = fuel_type
    
    def describe(self):
        super().describe()
        print(f"  Fuel type: {self.fuel_type}")

class ElectricCar(Car):
    def __init__(self, brand, model, max_speed, battery_kwh):
        super().__init__(brand, model, max_speed, fuel_type = 'electric')
        self.battery_kwh = battery_kwh

    def describe(self):
        super().describe()
        print(f"  Battery capacity: {self.battery_kwh}")



Vehicle1 = Vehicle("Yamaha", "MT-07", 200)
Vehicle1.describe()

Car1 = Car("Toyota", "Corolla", 180, "petrol")
Car1.describe()


CarElectric = ElectricCar("Tesla", "Model S", 250, 100)
CarElectric.describe()

