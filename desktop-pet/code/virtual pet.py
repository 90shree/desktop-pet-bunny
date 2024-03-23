import tkinter as tk
import time
import random

class Bunny:
    def __init__(self):
        # initialize tkinter window
        self.window = tk.Tk()
        self.window.config(highlightbackground='purple')
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        self.window.wm_attributes('-transparentcolor', 'purple')

        # load gifs
        self.load_gifs()

        # initialize variables
        self.init_variables()

        # create label for the window
        self.label = tk.Label(self.window, bd=0, bg='purple')
        self.label.pack()

        # dragging variables
        self.dragging = False
        self.start_x = 0
        self.start_y = 0

        # mouse events
        self.label.bind("<ButtonPress-1>", self.start_drag)
        self.label.bind("<B1-Motion>", self.drag)
        self.label.bind("<ButtonRelease-1>", self.release_drag)

        # start animation
        self.update()
        self.window.mainloop()

    def load_gifs(self):
        self.idle = tk.PhotoImage(file='idle.gif')
        self.walk_left = [tk.PhotoImage(file='walkleft.gif', format='gif -index %i' % i) for i in range(6)]
        self.walk_right = [tk.PhotoImage(file='walkright.gif', format='gif -index %i' % i) for i in range(6)]

    def init_variables(self):
        self.img = self.idle  # initialize img with the idle gif
        self.y = self.window.winfo_screenheight() - 110  # places in y-dir at bottom of the screen
        self.x = (self.window.winfo_screenwidth() - 110) / 2  # center horizontally
        self.vel_x = 0
        self.vel_y = 0
        self.gravity = 0.5
        self.last_change_time = time.time()

    def update(self):
        self.update_movement()
        self.update_window()
        self.window.after(10, self.update)

    def update_movement(self):
        current_time = time.time()
        if not self.dragging and current_time > self.last_change_time + 5:
            self.last_change_time = current_time
            random_action = random.choice(['idle', 'left', 'right'])
            if random_action == 'idle':
                self.img = self.idle
            elif random_action == 'left':
                self.img = random.choice(self.walk_left)
            elif random_action == 'right':
                self.img = random.choice(self.walk_right)

        if not self.dragging:
            self.vel_y += self.gravity
            self.y += self.vel_y

            # check if bunny reaches the bottom of the screen
            if self.y > self.window.winfo_screenheight() - 110:
                self.y = self.window.winfo_screenheight() - 110
                self.vel_y = 0

    def update_window(self):
        self.window.geometry('110x110+{x}+{y}'.format(x=str(int(self.x)), y=str(int(self.y))))
        self.label.configure(image=self.img)
        self.label.pack()

    def start_drag(self, event):
        self.dragging = True
        self.start_x = event.x
        self.start_y = event.y

    def drag(self, event):
        if self.dragging:
            self.x += event.x - self.start_x
            self.y += event.y - self.start_y
            self.start_x = event.x
            self.start_y = event.y

    def release_drag(self, event):
        self.dragging = False

Bunny()


        
        



                 
