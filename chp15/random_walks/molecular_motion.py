# Modify rw_visual.py by replacing ax.scatter() wtih ax.plot().
# To stimulate the path of a pollen grain on the surface of a drop of water, pass in the rw.x_values and rw.y_values,
# and incluce a linewidth argument
# Use 5000 instead of 50,000 points.

import matplotlib.pyplot as plt

from random_walk import Randomwalk

while True:
	# Make a random walk.
	rw = Randomwalk(5000)
	rw.fill_walk()

	# Plot the points in the walk.
	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(15,9))
	point_numbers = range(rw.num_points)
	ax.plot(rw.x_values, rw.y_values, linewidth=5)

	# Emphasize the first and last points.
	# ax.plot(0, 0, c='green')
	# ax.plot(rw.x_values[-1], rw.y_values[-1], c='red')

	# Remove the axes.
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

	plt.savefig('molecular_motion.png', bbox_inches='tight')
	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break