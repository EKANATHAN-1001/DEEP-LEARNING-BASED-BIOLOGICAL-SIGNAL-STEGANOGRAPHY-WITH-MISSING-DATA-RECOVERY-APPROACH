import serial
import time
import csv

# Open serial connection
ser = serial.Serial('COM5', 9600)  # Replace 'COMX' with your Arduino's port

# Open file for writing
filename = 'ecg_data.txt'
with open(filename, 'w') as file:
    start_time = time.time() 
    while time.time() - start_time <= 10:
        line = ser.readline().decode('utf-8').strip()
        print(line)  
        file.write(line + '\n')
        file.flush()  

# Input and output file names
input_filename = 'ecg_data.txt'
output_filename = 'ecg_data.csv'

# Read data from the text file
with open(input_filename, 'r') as infile:
    data = infile.readlines()

# Write data to CSV file with sequential numbering for the time column
with open(output_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Time', 'DATA'])  # Write header
    for i, line in enumerate(data, start=1):
        line = line.strip()  # Remove leading/trailing whitespace
        if line:  # Skip empty lines
            writer.writerow([i, line])  # Write data with sequential time
