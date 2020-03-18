# Try using Matplotlib to make a die-rolling visualization.
import matplotlib.pyplot as plt
import numpy as np

from die import Die

# Create a D6
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
	result = die.roll()
	results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# Visulize the results.
# Matplotlib
plt.style.use('seaborn-dark')
fig, ax  = plt.subplots(figsize=(15,9))

y_pos = np.arange(len(frequencies))
x_values = list(range(1, die.num_sides+1))

ax.bar(y_pos, x_values, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(frequencies)
ax.set_ylabel('Frequency of Result')
ax.set_xlabel('Result')
ax.set_title('Result of rolling one D6 die 1000 times')

plt.savefig('one_D6_bar_matplotlib.png', bbox_inches='tight')
plt.show()
