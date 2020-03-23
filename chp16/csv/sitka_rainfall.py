import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# Get dates and precipitation data
	dates, prcps = [],[]
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		dates.append(current_date)
		prcp = float(row[3])
		prcps.append(prcp)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(15,9))
ax.plot(dates, prcps, c='purple')

# Format plot
title = "Daily precipitation - 2018\nSita, AK"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitation (in)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig('sitka_precipitation_2018.png', bbox_inches='tight')
plt.show()