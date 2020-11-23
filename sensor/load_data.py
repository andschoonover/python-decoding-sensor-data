import os
import glob
import csv


#create a function to parse the data
def load_sensor_data(): 	#defined a function
	sensor_data = []		#set variable to an empty list

#create a variable and set it to call the glob.glob() function.

	sensor_files = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))
# Read data files

	for sensor_file in sensor_files:
		with open(sensor_file, r) as data_file:
			data_reader = csv.DictReader(data_file, delimiter = ',')
#load data records -> now that you have access to the data in each file, the next step is to load each record into the sensor_data list

			# create a second for look to get access to each record
			for row in data_file:
				#append each row record to the sens_data list
				load_sensor_data.append(row)
	print(sensor_data())
