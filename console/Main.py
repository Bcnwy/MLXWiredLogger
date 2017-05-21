from datetime import datetime
from time import time
import serial
import csv

# serial port parameters
_Port = 'COM5'
_Baudrate = 9600
# path = local root
_file = ("{}-MLX.csv".format(datetime.now().date()))

if __name__ == '__main__':

    serial = serial.Serial(port=_Port, baudrate=_Baudrate)
    #print _file
    # make file
    with open(_file, 'ab') as csvFile:
        writer = csv.writer(csvFile, dialect='excel')
        # write a new row the the csv file
        header = 'Sensor', 'Object', 'Ambient', 'Distance', 'uM_Time', 'Time'
        writer.writerow([datetime.now().__str__()])
        writer.writerow(header)
    csvFile.close()

    # start of EPOCH time
    startTime = time()
    while 1:
        read = serial.readline().strip()  # Read data
        rTime = time() - startTime  # get running time
        # format the sensor data
        d = read.split(',')
        d += {rTime.__str__()}
        print d
        # open csv file and set a writer to access the file
        with open(_file, 'ab') as csvFile:
            writer = csv.writer(csvFile, dialect='excel')
            # write a new row the the csv file
            writer.writerow(d)
    csvFile.close()
    serial.close()
