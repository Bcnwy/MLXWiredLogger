import Tkinter as Tk
import ttk
from datetime import datetime
from time import time
import serial
import csv

# serial port parameters
_Port = 'COM6'
_Baudrate = 57600
# path = local root
_file = ("{}-MLX.csv".format(datetime.now().date()))
_config = "config.cfg"

class App:
    def __int__(self, master):
        #Tk.Tk.__init__(self, *args)
        # Tk.Tk.wm_title(self, "MLX Interface")
        root = Tk.Frame(master)
        root.pack()
        self.ttk.Button(root, "help").pack()  # side="top", fill="both", expand=True

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        self.frames = {}

        # for F in (HomePage, CalPage):
        frame = HomePage(root, self)
        self.frames[HomePage] = frame
        frame.grid(row=0, colum=0, sticky="nsew")
        print "for loop"
        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frame[cont]
        frame.tkraise()


class HomePage(Tk.Frame):
    def __int__(self, parent, controller):
        Tk.Frame.__init__(self, parent)
        calibrate_bn = ttk.Button(self, text="Calibrate").pack()
        measure_bn = ttk.Button(self, text="Measure").pack()
        print "homepage"


class CalPage(Tk.Frame):
    def __int__(self, parent, controller):
        Tk.Frame.__init__(self, parent)
        print "calpage"



# if __name__ == '__main__':
root = Tk.Tk()
myApp = App(root)
#myApp.title("MLX Interface")
root.mainloop()

"""serial = serial.Serial(port=_Port, baudrate=_Baudrate)
print _file
# make file
with open(_file, 'ab') as csvFile:
    writer = csv.writer(csvFile, dialect='excel')
    # write a new row the the csv file
    header = 'Sensor', 'Object', 'Ambient', 'Distance', 'Time'
    writer.writerow([datetime.now().__str__()])
    writer.writerow(header)
csvFile.close()

# start of EPOCH time
startTime = time()
i = 0
while 1:

    read = serial.readline().strip()  # Read data
    rTime = time() - startTime  # get running time
    # format the sensor data
    d = read.split(',')
    d += {rTime.__str__()}
    print d
    i += 1
    # open csv file and set a writer to access the file
    with open(_file, 'ab') as csvFile:
        writer = csv.writer(csvFile, dialect='excel')
        # write a new row the the csv file
        writer.writerow(d)

csvFile.close()
serial.close()"""
