import serial
import time
import Tkinter
 
def quit():
    global tkTop
    tkTop.destroy()
 
def setCheckButtonText():
    if varCheckButton.get():
        varLabel.set("ALLUMER")
        ser.write(bytes('A'))
    else:
        varLabel.set("ETEINDRE")
        ser.write(bytes('E'))
 
locations=['/dev/ttyACM0', '/dev/ttyUSB0','/dev/ttyUSB1','/dev/ttyUSB2','/dev/ttyUSB3',
'/dev/ttyS0','/dev/ttyS1','/dev/ttyS2','/dev/ttyS3']

for device in locations:
    try:
        ser = serial.Serial(device, 38400)
        print "Connexion sur", device
    except:
        print "Echec de connexion sur", device

print("Reinitialiser Arduino")
time.sleep(3)
ser.write(bytes('E'))
 
tkTop = Tkinter.Tk()
tkTop.geometry('300x200')
 
varLabel = Tkinter.StringVar()
tkLabel = Tkinter.Label(textvariable=varLabel)
tkLabel.pack()
 
varCheckButton = Tkinter.IntVar()
tkCheckButton = Tkinter.Checkbutton(
    tkTop,
    text="Controle des DELs Arduino",
    variable=varCheckButton,
    command=setCheckButtonText)
tkCheckButton.pack(anchor=Tkinter.CENTER)
 
tkButtonQuit = Tkinter.Button(
    tkTop,
    text="Quitter",
    command=quit)
tkButtonQuit.pack()
 
Tkinter.mainloop()
