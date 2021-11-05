import car
from car import Car,ElectricCar

my_beetle = car.Car('volkswagen','beetle',2019)
my_car = Car('audi','a4',2019)
my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()