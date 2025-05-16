from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
import pygame
from pygame import mixer

mixer.init()
root = Tk()
root.geometry("1000x550")

def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    global img
    
    # Fix the filename - change to a proper GIF file that exists in your directory
    # You might need to update this to the actual filename you have
    gif_file = "gfggf.gif"
    
    mixer.music.load("music.mp3")
    mixer.music.play()
        
    try:
        img = Image.open(gif_file)
        lbl = Label(root)
        lbl.place(x=0, y=0)
        for img in ImageSequence.Iterator(img):
            img = img.resize((1000, 550))
            img = ImageTk.PhotoImage(img)
            lbl.config(image=img)
            root.update()
            time.sleep(0.05)
        root.deiconify()
    except FileNotFoundError:
        print(f"Error: The file '{gif_file}' doesn't exist in the current directory.")
        print(f"Current working directory: {os.getcwd()}")
        # Create a simple placeholder instead of the GIF
        lbl = Label(root, text="GIF file not found", font=("Arial", 24))
        lbl.pack(expand=True)
        
    

# Add this import for getting current directory
import os

play_gif()
root.mainloop()