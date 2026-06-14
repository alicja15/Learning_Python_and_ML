class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius
    
    def get_celsius(self):
        return self.__celsius
    def set_celsius(self, value):
        if value >= -273.15:
            self.__celsius = value
        else:
            print("Temperature too low")
    def get_fahrenheit(self):
        return (self.__celsius * 9/5) + 32
    

t = Temperature(25)
print(f"{t.get_celsius()}°C is {t.get_fahrenheit()}°F")

