import csv

filename = 'data/MODIS_C6_Global_7d.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	for index, column_header in enumerate(header_row):
		print(index, column_header)