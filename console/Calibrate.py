from datetime import datetime
from time import time
import serial.tools.list_ports
import serial
import sys
import csv
import os
import json

_calFile = "cal.txt"
# serial port parameters
_Baudrate = 9600


class MLX:
    global temp

    def __init__(self):
        ports = list(serial.tools.list_ports.comports())
        for com in ports:
            print com
        print "Select Com Port: "
        comport = raw_input()
        _Port = "COM{}".format(int(comport))
        try:
            com = self.serial.Serial(port=_Port, baudrate=_Baudrate)
        except:
            print "Failed to open serial port"
            pass

    @staticmethod
    def calibrate(self):
        global temp
        for i in range(1,40 ):
            try:
                r = self.serial.readline().strip()  # Read data
                read = json.loads(r)
            except:
                pass
            temp[read['Sensor']] = read['obj']

        print temp


if __name__ == '__main__':

    with open(_calFile, 'ab') as csvFile:
        writer = csv.writer(csvFile, dialect='excel')
        # write a new row the the csv file
        writer.writerow([datetime.now().__str__()])
    csvFile.close()
    # start of EPOCH time
    startTime = time()
    mlx = MLX()
    while 1:
        rTime = time() - startTime  # get running tim
        mlx.calibrate()
    serial.close()
