#!/usr/bin/python
# Used on Raspbian GNU/Linux 8.0 (jessie)
# Created 6/28/19 by Thomas Chemmanoor

#importing time, GPIO, and tkinter libraries as needed

import time
import datetime
import RPi.GPIO as GPIO

from tkinter import *
from tkinter import ttk
from tkinter import font
from stopwatch import Stopwatch


#initializing the GPIO pin 18 to be an input

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#initializing the stopwatch and then resetting since creating a stopwatch instance immediately starts he stopwatch clock

sw = Stopwatch()
sw.reset()


rst = True;
running = True;


# Function: quit()
# Param: *args
# This function closes the tkinter instance
def quit(*args):
    root.destroy()

# Function: show_time()
# This function constantly updates the time and checks both system states to start a stopwatch when the button is pressed
# and display a nice message when the button is not pressed (when the dog is being walked).

def show_time():
    # Show the time right now
    txt1.set(datetime.datetime.now().strftime("Time:   %-I:%M:%S"))
    global running
    global rst
    if running == False:
        #send formatted str(sw) to aws to log time
        sw.stop()
        txt.set('HAVE FUN')
        txt2.set('ON YOUR WALK!')
    else:
        if rst == True:
            sw.reset() 
            sw.start()
            rst = False
        time.sleep(.3)
        txt.set('SINCE LAST WALK:')
        txt2.set(str(datetime.timedelta(seconds = int(sw.duration))))
    root.after(1000, show_time)

# Function: timeSinceLastStopwach
# Param: GPIO channel
# This function uses the value of the button press connected to GPIO pin 18 to switch between running and reset states

def timeSinceLastStopwatch(channel):
    global rst
    global running
    if GPIO.input(18):
        rst  = True
        running = False        
    else:
        running = True

# Setting up the tkinter instance and calling the function to update the timer constantly 

root = Tk()
root.attributes("-fullscreen", True)
root.configure(background='black')
root.bind("x", quit)
root.after(1000, show_time)

# Setting up the three tkinter text fields and labels

fnt = font.Font(family='Helvetica', size=100, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="green", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

txt1 = StringVar()
lbl1 = ttk.Label(root, textvariable=txt1, font=fnt, foreground="green", background="black")
lbl1.place(relx=0.5, rely=0.2, anchor=CENTER)

txt2 = StringVar()
lbl2 = ttk.Label(root, textvariable=txt2, font=fnt, foreground="green", background="black")
lbl2.place(relx=0.5, rely=0.8, anchor=CENTER)

# Adding a GPIO event instead of polling to lessen CPU strain. This callback runs the function timeSinceLastStopwatch everytime the button switches states (being pressed/ being released)

GPIO.add_event_detect(18,GPIO.BOTH, callback=timeSinceLastStopwatch, bouncetime=300)

# Constantly updating tkinter instance
root.mainloop()
