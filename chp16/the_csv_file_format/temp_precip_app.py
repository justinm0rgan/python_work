# To use this program, the arguments are as follows...
# python3 precip_app.py <CSV FILE> <DATE COLUMN NUMBER> <PRECIPITATION COLUMN NUMBER> <CHART TITLE> <OUTPUT IMAGE FILENAME>
#
# Example usage:
# python3 precip_app.py 'data/sitka_weather_2018_simple.csv' 2 3  "Daily precipitation - 2018\nSita, AK" "sitka_precipitation_2018.png"

import csv
import matplotlib.pyplot as plt
import sys
from datetime import datetime
# from date_parser import DateParser
from dateutil.parser import parse


# Get all the input from the user
csv_file = sys.argv[1]
date_column_number = int(sys.argv[2])
precip_data_column_number = int(sys.argv[3])
chart_title = sys.argv[4]
output_png_file_name = sys.argv[5]

with open(csv_file) as f:
	reader = csv.reader(f)
	header_row = next(reader)

    # Get dates and precipitation data
	dates, prcps = [],[]

	for row in reader:
		parsed_date = parse(row[date_column_number])
		# parser = DateParser(row[date_column_number])
		# parsed_date = parser.parse()
		datetime.strftime(parsed_date, '%Y-%m-%d')

		if parsed_date != None:
			dates.append(parsed_date)

		if row[precip_data_column_number] == '':
			prcps.append(0.0)
		else:
			parsed_precipitation = float(row[precip_data_column_number])
			prcps.append(parsed_precipitation)

# Plot the points.
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(15,9))
ax.plot(dates, prcps, c='purple')

# Format labels
title = chart_title
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Precipitation (in)", fontsize=16)

# Format the ticks
plt.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate()


plt.savefig('./output/' + output_png_file_name, bbox_inches='tight')
plt.show()