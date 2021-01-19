import threading
from tkinter import *
from style import *
from threading import Thread
import os
import random
import time


def get_music_files():
    files = os.listdir('files')
    return files


def run_music():
    while True:
        music_files = get_music_files()
        shuffled_music = random.choice(music_files)
        shuffled_music_full_path = os.path.join(os.curdir, 'files', shuffled_music)  # grab all the paths together
        os.startfile(shuffled_music_full_path)
        print(shuffled_music_full_path)
        time.sleep(30)


root = Tk()
root.configure(bg=blue)
root.geometry("480x320")

title = Label(root, text="Music Program",
              fg=yellow, bg=blue,
              font=(font_type, 36)
              )
title.pack()

sub_title = Label(root, text="Click the button to start playing music",
                  fg=yellow, bg=blue,
                  font=(font_type, 18)
                  )
sub_title.pack()

run_music_button = Button(root, text="Play Music!",
                          command=run_music,
                          fg=yellow, bg=blue,
                          font=(font_type, 24)
                          )
run_music_button.pack(side=BOTTOM)
root.mainloop()
