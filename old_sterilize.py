# !/usr//bin/python3
from tkinter import *
import time
from tkinter.messagebox import showinfo
from uart_port import Serial_Port

#create tkinter as win
win = Tk()

serial_port = Serial_Port(port_name="/dev/ttyACM0")

#### functions call #######
def exitProgram():
    print("Exit Button pressed")
    win.quit()
    
def washing():
    current_state.config(text = "Washing!") #change text to washing
    serial_port.write_serial_message("1")
    #countdownTimer(30) #give it 30seconds to run

def sterilize():
    current_state.config(text = "Sterilizing!")
    serial_port.write_serial_message("2")
    #countdownTimer(20)    
        
def drying():
    current_state.config(text = "Drying!")
    serial_port.write_serial_message("3")
    #countdownTimer(120)
    
#run all will have 0.5s buffer for text to change properly
#win,after is in milli seconds and after the command will
#run the commands above with the bracket
def runAll():
    serial_port.write_serial_message("1")
    win.after(500, washing)

    serial_port.write_serial_message("2")
    win.after(32000,sterilize)

    serial_port.write_serial_message("3")
    win.after(53500,drying)


#main function
def countdownTimer(timer):
    #change the timer to the int passed into the function
    washBtn.config(state="disable")
    sterilizeBtn.config(state="disable")
    dryBtn.config(state="disable")
    runAllBtn.config(state="disable")
    timer_display.config(text = timer)
    if timer >= 0:
        #count down
        win.after(1000,countdownTimer,timer-1)
        if timer == 0:
            showinfo(title = "Timer Countdown", message= "Time's up")
            washBtn.config(state="active")
            sterilizeBtn.config(state="active")
            dryBtn.config(state="active")
            runAllBtn.config(state="active")
        #constantly updates the text of the count down timer
        timer_display.config(text = timer)
    else:
        current_state.config(text = "Idling!")    
        timer_display.config(text = '00')
        
global timer_display, sec
win.title("Sterilising Syringe Control")
#size of the window
win.geometry('800x480')
#background color
win.configure(bg='skyblue4')

#configurations of all the buttons
exitBtn = Button(win, text = "Exit", font=('Helvetica bold', 30),
                 command = exitProgram,height = 1, width = 6)
exitBtn.pack(side = BOTTOM)

washBtn = Button(win, text = "Wash Only", font=('Helvetica bold', 15),
                      command = washing, height = 2, width = 10)
washBtn.pack(padx=120, pady=5, side = LEFT)

sterilizeBtn = Button(win, text = "Sterilize Only", font=('Helvetica bold', 15),
                      command = sterilize, height = 2, width = 10)
sterilizeBtn.pack(padx=120, pady=5, side = RIGHT)

dryBtn = Button(win, text = "Dry Only", font=('Helvetica bold', 15),
                command = drying,height = 2, width = 10)
dryBtn.place(x=120, y =250)

runAllBtn = Button(win, text = "Run All", font=('Helvetica bold', 15),
                   command = runAll, height = 2, width = 10)
runAllBtn.place(x=520,y =250)

#Create Timer Label and Timer widgets
current_state = Label(win,text = "Idling!", bg = 'skyblue4',fg = "IndianRed1",
      font=('Helvetica bold', 22))
current_state.place(x=370, y=20)

Label(win,text = "Timer:", bg = 'skyblue4',fg = "IndianRed1",
      font=('Helvetica bold', 14)).place(x=370, y=70)
timer_display = Label(win, text = "00", width = 3, bg = 'skyblue4',
      fg = 'IndianRed2', font = ('Helvetica bold', 14))
timer_display.place(x=430,y=70)

#run win as a loop
mainloop()

