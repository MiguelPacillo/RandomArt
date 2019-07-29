from tkinter import *
import random

window = Tk()
window.title("Random Art")
window.resizable(0, 0)
window.configure(background="white")
window.geometry("500x500")

canvas = Canvas(window, height=450, width=500, bg="white")
canvas.pack()

def shape():

    pointnum = random.randint(1, 100)*2
    points = random.sample(range(1, 450), pointnum)
    colors = ["red", "blue", "orange", "black"]
    canvas.create_polygon(points, outline=random.choice(colors), fill=random.choice(colors))

shape()
window.mainloop()