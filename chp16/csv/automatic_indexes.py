# Use header row to determine the indexes corresponding to the TMIN and TMAX columns.
# Use the header row to determine the indexes for these values, so your program can work for Sitka or Death Valley
# Use the station name to automatically generate an appropiate title for your graph as well.

import csv

import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# Get dates, high and low temperatures from this file.
	dates, highs, lows = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		if header_row == 'TMIN':
			low = row_tmin
		if header_row == 'TMAX':
			high = row_tmax
			try:
				high = int(row_tmin)
				low = int(row_tmax)
			except ValueError:
				print(f"Missing data for {current_date}")
			else:
				dates.append(current_date)
				highs.append(high)
				lows.append(low)


# Graphing code
# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.6)
ax.plot(dates, lows, c='blue', alpha=0.6)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
title = (f"{row[2]}")
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylim(20,130)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# plt.savefig('death_valley_2018_daily_hi_low_temp.png', bbox_inches='tight')
plt.show()
