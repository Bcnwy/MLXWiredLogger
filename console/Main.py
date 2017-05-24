from datetime import datetime
from time import time
import serial
import csv
import ijson
import json

# serial port parameters
_Port = 'COM5'
_Baudrate = 9600
# path = local root
_file = ("{}-MLX.txt".format(datetime.now().date()))

if __name__ == '__main__':

    serial_port = serial.Serial(port=_Port, baudrate=_Baudrate)
    # print _file
    # make file
    with open(_file, 'a') as csvFile:
        writer = csv.writer(csvFile, dialect='excel')
        # write a new row the the csv file
        header = 'Sensor', 'Object', 'Ambient', 'DistanceUltra', 'DistanceTOF', 'uTime', 'Time'
        # writer.writerow([datetime.now().__str__()])
        writer.writerow(header)
    csvFile.close()

    # start of EPOCH time
    # global startTime
    startTime = time()
    while 1:
        try:
            read = serial_port.readline().decode('utf-8').rstrip()  # Read data
            #  format the sensor data
            d = json.loads(str(read))
            print(d)
        except:
            pass

        rTime = time() - startTime  # get running time

        # open csv file and set a writer to access the file
        with open(_file, 'a') as csvFile:
            writer = csv.writer(csvFile, dialect='excel')
            # write a new row the the csv file
            for mTemp in d:
                # print(mTemp)
                writer.writerow([mTemp['Sensor'],
                                mTemp['Obj'],
                                mTemp['Amb'],
                                mTemp['Dist'][0],
                                mTemp['Dist'][1],
                                mTemp['uTime'],
                                rTime])
    csvFile.close()
    serial.close()
