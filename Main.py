
from datetime import datetime
from time import time
import serial
import csv

# open csv file and set a writer to access the file
with open('some.csv', 'wb') as csvFile:
    writer = csv.writer(csvFile, dialect='excel')
# serial port parameters
_Port = 'COM5'
_Baudrate = 460800

if __name__ == '__main__':

    serial = serial.Serial(port=_Port, baudrate=_Baudrate)
    i = 0
    while i < 50:
        rTime = time()  # get timestamp
        read = serial.readline()  # Read data

        # format the sensor data
        d = read.split(',')
        name = d[0]
        objTemp = d[1]
        abiTemp = d[2]
        dist = d[3]

        # output data to console
        print name + ',' + objTemp + ',' + rTime

        # write a new row the the csv file
        writer.writerow(d)

        i += 1
    serial.close()
    csvFile.close()
