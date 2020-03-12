import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1,8,27,64,125]

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# Set chart title and label axis
ax.set_title('Cubed Numbers', fontsize=26)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Cube of Value', fontsize=12)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=10)

plt.show()
