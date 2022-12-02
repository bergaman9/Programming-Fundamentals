""" A Brief Study in Handling Life Events """

import tkinter
import time

# handler for timer event
def alarm():
    print('Calling the Pizza Company.')
    
# handler for ringing doorbell
def doorbell():
    print('Ding Dong!')
    time.sleep(4)
    print('Opening the Door')

# handler for when the phone rings
def phonecall():
    print('Answering the phone.')
    
# create buttons and assign callbacks    
root = tkinter.Tk()
tkinter.Button(root, text='Ring Doorbell', command=doorbell).pack()
tkinter.Button(root, text='Call Phone', command=phonecall).pack()

# set a timer for 1 second
root.after(4000, alarm)

# start the event loop
root.mainloop()
