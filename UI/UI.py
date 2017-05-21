import Tkinter as Tk
import ttk
import serial.tools.list_ports
import Cal

_baudrate = '9600'


class App(Tk.Tk):
    def __init__(self, *args):
        Tk.Tk.__init__(self, *args)
        Tk.Tk.wm_title(self, "MLX Interface")
        Tk.Tk.iconbitmap(self, default="MLX.ico")
        root = Tk.Frame()
        root.pack()
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (HomePage, CalPage, MeasurePage):
            frame = F(root, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class HomePage(Tk.Frame):
    def __init__(self, parent, controller):
        Tk.Frame.__init__(self, parent)
        m_comport = Tk.StringVar()
        ports = serial.tools.list_ports.comports()
        m = Tk.OptionMenu(self, m_comport, ports)
        m.pack()
        calibrate_bn = ttk.Button(self, text="Calibrate", command=lambda: controller.show_frame(CalPage))
        calibrate_bn.pack(fill="both", expand=True)
        measure_bn = ttk.Button(self, text="Measure", command=lambda: controller.show_frame(MeasurePage))
        measure_bn.pack(fill="both", expand=True)


class CalPage(Tk.Frame):
    def __init__(self, parent, controller):
        self.parent = parent
        Tk.Frame.__init__(self, parent)

        Cal.CalOffsets('COM5', '9600')


class MeasurePage(Tk.Frame):
    def __init__(self, parent, controller):
        self.parent = parent
        Tk.Frame.__init__(self, parent)

if __name__ == '__main__':
    myApp = App()
    myApp.wm_minsize(width=200, height=200)
    myApp.mainloop()