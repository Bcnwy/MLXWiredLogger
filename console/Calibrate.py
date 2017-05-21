from datetime import datetime
from time import time
import serial
import serial.tools.list_ports
import sys
import csv

_calFile = "cal.txt"
# serial port parameters
_Baudrate = 9600

if __name__ == '__main__':
    ports = list(serial.tools.list_ports.comports())
    for com in ports:
        print com
    print "Select Com Port: "
    comP = raw_input()
    _Port = "COM{}".format(int(comP))
    try:
        serial = serial.Serial(port=_Port, baudrate=_Baudrate)
    except:
        print "Failed to open serial port"
        pass

    with open(_calFile, 'ab') as csvFile:
        writer = csv.writer(csvFile, dialect='excel')
        # write a new row the the csv file
        writer.writerow([datetime.now().__str__()])
    csvFile.close()

    # start of EPOCH time
    startTime = time()
    while 1:
        try:
            read = serial.readline().strip()  # Read data
        except:
            pass
        rTime = time() - startTime  # get running time
        # format the sensor data
        d = read.split(',')
        


    with open(_file, 'ab') as csvFile:
        writer = csv.writer(csvFile, dialect='excel')
        # write a new row the the csv file
        writer.writerow(d)
    csvFile.close()
    serial.close()
