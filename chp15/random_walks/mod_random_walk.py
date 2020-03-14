# Modify values in x and y lists to see what happens to the overall shape of your walks.
# Try a longer list of choices for the distance, such as 0 through 8, or remove the -1
# from the x or y direction list.

from random import choice

class Randomwalk:
	"""A class to generate random walks"""

	def __init__(self, num_points=5000):
		"""Initialize attributes of a walk."""
		self.num_points = num_points


	# All walks start at (0, 0)
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self):
		"""Calculate all the points in the walk."""

		# Keep taking steps until the walk reaches the desired length.
		while len(self.x_values) < self.num_points:

			# Decide which direction to go and how far to go in that direction.
			x_direction = choice([1,-1])
			x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
			x_step = x_direction * x_distance

			y_direction = choice([1,-1])
			y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
			y_step = y_direction * y_distance

			# Reject moves that go nowhere.
			if x_step == 0 and y_step == 0:
				continue

			# Calculate the new postion.
			x = self.x_values[-1] + x_step
			y = self.y_values[-1] + y_step

			self.x_values.append(x)
			self.y_values.append(y)