import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# Set chart title and label axis
ax.set_title('Cubed Numbers', fontsize=26)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Cube of Value', fontsize=12)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=10)

# Set the range for each axis
ax.axis([0, 5001, 0, 125000000000])

plt.show()
