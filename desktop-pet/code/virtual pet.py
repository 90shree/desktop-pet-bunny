import random
import tkinter as tk
import pyautogui

x = 1400
cycle = 0
check = 1
idle_num =[1,2,3,4]
sleep_num = [10,11,12,13,15]
walk_left = [6,7]
walk_right = [8,9]
event_number = random.randrange(1,3,1)
impath = 'bunny.png'

window = tk.Tk()

##use this for every animation
idle_animation = [tk.PhotoImage(file=impath+'idle.gif',format='gif -index %i'%(i))for i in range (x)] #replace x with num frames
yawn = [tk.PhotoImage(file=impath+'yawn.gif',format='gif -index %i'%(i))for i in range (x)]
idle_to_sleep = [tk.PhotoImage(file=impath+'idle_to_sleep.gif',format='gif -index %i'%(i))for i in range (x)]


sleep = [tk.PhotoImage(file=impath+'sleeping.gif',format='gif -index %i'%(i))for i in range (x)]
sleep_to_idle = [tk.PhotoImage(file=impath+'wake_up.gif',format='gif -index %i'%(i))for i in range (x)]

eat = [tk.PhotoImage(file=impath+'eat.gif',format='gif -index %i'%(i))for i in range (x)]
eat_to_sleep = [tk.PhotoImage(file=impath+'fall_asleep.gif',format='gif -index %i'%(i))for i in range (x)]

walk_forward = [tk.PhotoImage(file=impath+'walk_f.gif',format = 'gif -index %i' %(i)) for i in range(x)
walk_backward = [tk.PhotoImage(file=impath+'walk_b.gif',format = 'gif -index %i' %(i)) for i in range(x)



##makes background from black to transparent
window.config(highlightbackground='black')
window.overideredirect(True)
window.wm_attributes('-transparentcolor','black')

##assign label to make it movable and animated at the same time
label = tk.Label(window,bg = 0,bg = 'black')
label.pack()
windows.mainloop()

##loop each gif frame
def loop(cycle,frames,event_num,first_num,last_num)
    if (cycle < len(frames)) -1:
        cycle += 1

def update(cycle,check,event_number,x):
    ##idle
    if check == 0:
        frame = idle[cycle]
        cycle,event_num = loop(cycle,idle,event_num,1,9)

    ##idle to sleep
    elif check == 1:
        frame = idle_to_sleep[cycle]
        cycle,event_num = loop(cycle,idle_to_sleep,event_num,10,10)

    ##sleep
    elif check == 2:
        frame = sleep[cycle]
        cycle,event_num = loop(cycle,sleep,event_num,10,15)

    ##sleep to idle
    elif check == 3:
        frame = sleep_to_idle[cycle]
        cycle,event_num = loop(cycle,sleep_to idle,event_num,1,1)

    ##walk forward
    elif check == 4:
        frame = walk_positive[cycle]
        cycle,event_num = loop(cycle,walk_forward,event_num,1,9)
        x -= 3
        
    ##walk forward
    elif check == 5:
        frame = walk_positive[cycle]
        cycle,event_num = loop(cycle,walk_backward,event_num,1,9)
        x -= 3

    window.geometry('100x100+'+str(x)+'+1050')
    label.configure(image=frame)
    window.after(1,event,cycle,check,event_num,x)

    

        
        



                 
