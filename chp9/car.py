"""A class that can be used to represent a car."""

class Car:
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""Initalize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.make} {self.model} {self.year}"
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage"""
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""Set the odomoter reading to the given value.
		Reject the change if it attempts to roll the odometer back
		"""
		if mileage >=self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!!!")

	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles

# class Battery:
# 	"""A simple attempt to model a battery for an electric car."""

# 	def __init__(self, battery_size=75):
# 		"""Initialize the battery's attributes."""
# 		self.battery_size = battery_size

# 	def describe_battery(self):
# 		"""Print a statement desciribng the battery size."""
# 		print(f"This car has a {self.battery_size}-kWh batter.")

# 	def get_range(self):
# 		"""Print a statement about the range this battery provides."""
# 		if self.battery_size == 75:
# 			range = 260
# 		elif self.battery_size == 100:
# 			range = 315

# 		print(f"This car can go about {range} miles on a full charge.")

# 	def upgrade_battery(self):
# 		"""Checks battery size and sets the capacity to 100"""
# 		if self.battery_size == 75:
# 			self.battery_size += 25

# class ElectricCar(Car):
# 	"""Represents aspects of a car, specifice to electric vehicles."""

# 	def __init__(self, make, model, year):
# 		"""Initalize aspects of the parent class.
# 		Then initialize attributes specific to an electric car."""
# 		super().__init__(make, model, year)
# 		self.battery = Battery()

# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()