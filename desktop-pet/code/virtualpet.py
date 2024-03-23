import tkinter as tk
import time
import random

class Bunny:
    def __init__(self):
        self.window = tk.Tk()
        self.window.config(highlightbackground='purple')
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        self.window.wm_attributes('-transparentcolor', 'purple')

        self.load_gifs()

        self.init_variables()

        self.label = tk.Label(self.window, bd=0, bg='purple')
        self.label.pack()

        self.dragging = False
        self.start_x = 0
        self.start_y = 0

        self.label.bind("<ButtonPress-1>", self.start_drag)
        self.label.bind("<B1-Motion>", self.drag)
        self.label.bind("<ButtonRelease-1>", self.release_drag)

        self.update()
        self.window.mainloop()

    def load_gifs(self):
        self.sleep = [tk.PhotoImage(file='sleep.gif', format='gif -index %i' % i) for i in range(7)]
        self.eat = [tk.PhotoImage(file='eat.gif', format='gif -index %i' % i) for i in range(13)]
        self.walk_left = [tk.PhotoImage(file='walkleft.gif', format='gif -index %i' % i) for i in range(6)]
        self.walk_right = [tk.PhotoImage(file='walkright.gif', format='gif -index %i' % i) for i in range(6)]
        self.idle = [tk.PhotoImage(file='idle.gif', format='gif -index %i' % i) for i in range(2)]

    def init_variables(self):
        self.current_action = None
        self.img = self.sleep[0]
        self.y = self.window.winfo_screenheight() - 110
        self.x = (self.window.winfo_screenwidth() - 110) / 2
        self.vel_x = 0
        self.vel_y = 0
        self.gravity = 9.81
        self.drag_acceleration = 0.5
        self.drag_deceleration = 9
        self.last_action_time = time.time()
        self.last_change_time = time.time()
        self.action_duration = 0

    def update(self):
        self.update_movement()
        self.update_window()
        self.window.after(10, self.update)

    def update_movement(self):
        current_time = time.time()

        if current_time > self.last_change_time + 7:
            self.last_change_time = current_time
            self.img = self.idle[0]
            self.action_duration = 5
            self.last_action_time = current_time

            if self.current_action is None:
                random_action = random.randint(1, 4)
                if random_action == 1:
                    self.current_action = 'sleep'
                    self.img_sequence = self.sleep
                    self.action_duration = 7
                elif random_action == 2:
                    self.current_action = 'eat'
                    self.img_sequence = self.eat
                    self.action_duration = 3
                elif random_action == 3:
                    self.current_action = 'walk_right'
                    self.img_sequence = self.walk_right
                    self.action_duration = 3.5
                elif random_action == 4:
                    self.current_action = 'walk_left'
                    self.img_sequence = self.walk_left
                    self.action_duration = 3.5
                time.sleep(3)

        if not self.dragging:
            self.vel_y += self.gravity
            self.y += self.vel_y

            if self.y > self.window.winfo_screenheight() - 110:
                self.y = self.window.winfo_screenheight() - 110
                self.vel_y = 0

        if hasattr(self, 'img_sequence'):
            num_frames = len(self.img_sequence)
            elapsed_time = current_time - self.last_action_time
            frame_index = int((elapsed_time / 0.1) % num_frames)
            self.img = self.img_sequence[frame_index]

            if self.current_action == 'walk_right':
                self.x += 1
                if self.x > self.window.winfo_screenwidth() - 110:
                    self.current_action = 'idle'
                    self.img = self.idle_blink[0]
            elif self.current_action == 'walk_left':
                self.x -= 1
                if self.x < 0:
                    self.current_action = 'idle'
                    self.img = self.idle[0]

        if current_time > self.last_action_time + self.action_duration:
            self.current_action = None
            self.img = self.idle[0]

    def update_window(self):
        self.window.geometry('110x110+{x}+{y}'.format(x=str(int(self.x)), y=str(int(self.y))))
        self.label.configure(image=self.img)
        self.label.pack()

    def start_drag(self, event):
        self.dragging = True
        self.start_x = event.x_root
        self.start_y = event.y_root

    def drag(self, event):
        if self.dragging:
            self.x = event.x_root - self.start_x + self.x
            self.y = event.y_root - self.start_y + self.y
            self.start_x = event.x_root
            self.start_y = event.y_root

    def release_drag(self, event):
        self.dragging = False

Bunny()
