# !/usr//bin/python3
import time
import sys
from tkinter import *
from tkinter.messagebox import showinfo
from uart_port import Serial_Port

#create tkinter as win
win = Tk()

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

if "-no-port" in opts:
    usePort = False
    serial_port = Serial_Port()
else:
    serial_port = Serial_Port(port_name="/dev/ttyACM0")

#### functions call #######
def write_to_serial(number):
    print(f'Input to write {number}')
    if usePort:
        serial_port.write_serial_message(number)

def exitProgram():
    print("Exit Button pressed")
    win.quit()
    
def washing():
    write_to_serial("1")
    current_state.config(text = "Washing!") #change text to washing
    countdownTimer(33) #give it 30seconds to run

def sterilize():
    write_to_serial("2")
    current_state.config(text = "Sterilizing!")
    countdownTimer(23)    
        
def drying():
    write_to_serial("3")
    current_state.config(text = "Drying!")
    countdownTimer(27)
    
#run all will have 0.5s buffer for text to change properly
#win,after is in milli seconds and after the command will
#run the commands above with the bracket
def runAll():
    win.after(500, washing)
    win.after(34000,sterilize)
    win.after(57500,drying)

#main function
def countdownTimer(timer):
    #change the timer to the int passed into the function
    washBtn.config(state="disabled", activebackground='skyblue4')
    sterilizeBtn.config(state="disabled", activebackground='skyblue4') 
    dryBtn.config(state="disabled", activebackground='skyblue4')
    runAllBtn.config(state="disabled", activebackground='skyblue4')
    exitBtn.config(state="disabled", activebackground='skyblue4')
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
            exitBtn.config(state="active")
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

#image buttons
exit_ImageBtn = PhotoImage(file='exit.png')
wash_ImageBtn = PhotoImage(file='wash.png')
sterilise_ImageBtn = PhotoImage(file='sterilization.png')
dry_ImageBtn = PhotoImage(file='dry.png')
runAll_ImageBtn = PhotoImage(file='runAll.png')
#configurations of all the buttons
#exitBtn = Button(win, text = "Exit", font=('Helvetica bold', 30),
#                 command = exitProgram,height = 1, width = 6,)
#dryBtn = Button(win, text = "Dry Only", font=('Helvetica bold', 15),
#                command = drying,height = 2, width = 10)
#runAllBtn = Button(win, text = "Run All", font=('Helvetica bold', 15),
#                   command = runAll, height = 2, width = 10)
exitText = Label(win,text="exit", bg='skyblue4', font=('Helvetica bold', 10),
                 fg = "grey1",borderwidth = 0, highlightthickness = 0)
exitText.pack(side=BOTTOM)
exitBtn = Button(win, image=exit_ImageBtn,
                 command=exitProgram, bg='skyblue4', borderwidth=0,
                 highlightthickness = 0)
exitBtn.pack(side = BOTTOM)

washBtn = Button(win, image = wash_ImageBtn,command = washing, bg='skyblue4',
                 borderwidth = 0, highlightthickness = 0)
washBtn.pack(padx=170, pady=3, side = LEFT)
washText = Label(win,text = "wash", bg = 'skyblue4',font=('Helvetica bold', 10),
                 fg = "grey1",borderwidth = 0, highlightthickness = 0)
washText.place(x=178,y=236)

sterilizeBtn = Button(win, image = sterilise_ImageBtn, command=sterilize,
                      bg='skyblue4',borderwidth = 0, highlightthickness = 0)
sterilizeBtn.pack(padx=170, pady=5, side = RIGHT)
sterilizeText = Label(win,text = "sterilise", bg = 'skyblue4',font=('Helvetica bold', 12),
                 fg = "grey1",borderwidth = 0, highlightthickness = 0)
sterilizeText.place(x=566,y=236)

dryBtn = Button(win, image= dry_ImageBtn, command=drying,
                bg='skyblue4',borderwidth = 0, highlightthickness = 0)
dryBtn.place(x=175, y =270)
dryText = Label(win,text = "dry", bg = 'skyblue4',font=('Helvetica bold', 12),
                 fg = "grey1",borderwidth = 0, highlightthickness = 0)
dryText.place(x=185,y=335)

runAllBtn = Button(win, image = runAll_ImageBtn, command=runAll,
                   bg='skyblue4',borderwidth = 0, highlightthickness = 0)
runAllBtn.place(x=565,y =280)
runAllText = Label(win,text = "Run All", bg = 'skyblue4',
                   font=('Helvetica bold', 10),fg = "grey1",
                   borderwidth = 0, highlightthickness = 0)
runAllText.place(x=570,y=338)
#Create Timer Label and Timer widgets
current_state = Label(win,text = "Idling!", bg = 'skyblue4',fg = "grey1",
      font=('Helvetica bold', 22),anchor=CENTER)
#current_state.pack()
current_state.place(x=370, y=20)

Label(win,text = "Timer:", bg = 'skyblue4',fg = "grey1",
      font=('Helvetica bold', 14)).place(x=270, y=70)
timer_display = Label(win, text = "00", width = 3, bg = 'skyblue4',
      fg = 'grey1', font = ('Helvetica bold', 14))
timer_display.place(x=330,y=70)

Label(win,text = "Temp:", bg = 'skyblue4',fg = "grey1",
      font=('Helvetica bold', 14)).place(x=450, y=70)
temp_display = Label(win, text = "26", width = 3, bg = 'skyblue4',
      fg = 'grey1', font = ('Helvetica bold', 14))
temp_display.place(x=510,y=70)

#run win as a loop
mainloop()



