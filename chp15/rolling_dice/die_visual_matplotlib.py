# Try using Matplotlib to make a die-rolling visualization.
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from die import Die

# Create a D6
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(10_000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# Visulize the results.
# Matplotlib
plt.style.use('seaborn-dark')
fig, ax  = plt.subplots(figsize=(15,9))

y_pos = frequencies
x_values = list(range(1, max_result+1))
tick_spacing = 1

plt.bar(x_values, y_pos)
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
plt.ylabel('Frequency of Result')
plt.xlabel('Result')
plt.title('Result of rolling two D6 dice 10_000 times')

plt.savefig('two_D6_bar_matplotlib.png', bbox_inches='tight')
plt.show()
