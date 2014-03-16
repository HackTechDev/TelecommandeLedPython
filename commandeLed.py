import serial
import time
import Tkinter
 
def quit():
    global tkTop
    tkTop.destroy()
 
def setCheckButtonText():
    if varCheckButton.get():
        varLabel.set("LED ON")
        ser.write(bytes('H'))
    else:
        varLabel.set("LED OFF")
        ser.write(bytes('L'))
 
ser = serial.Serial('/dev/ttyACM0', 9600)
print("Reset Arduino")
time.sleep(3)
ser.write(bytes('L'))
 
tkTop = Tkinter.Tk()
tkTop.geometry('300x200')
 
varLabel = Tkinter.StringVar()
tkLabel = Tkinter.Label(textvariable=varLabel)
tkLabel.pack()
 
varCheckButton = Tkinter.IntVar()
tkCheckButton = Tkinter.Checkbutton(
    tkTop,
    text="Control Arduino LED",
    variable=varCheckButton,
    command=setCheckButtonText)
tkCheckButton.pack(anchor=Tkinter.CENTER)
 
tkButtonQuit = Tkinter.Button(
    tkTop,
    text="Quit",
    command=quit)
tkButtonQuit.pack()
 
Tkinter.mainloop()
