filename = 'fire_index_data.txt'

with open(filename, 'a') as file_object:
	file_object.write("\nFire data:")
	file_object.write("\n\t 0 latitude\n1 longitude\n2 brightness\n3 scan\n4 track\n5 acq_date\n6 acq_time\n7 satellite\n8 confidence\n9 version\n10 bright_t31\n11 frp\n12 daynight")
	
