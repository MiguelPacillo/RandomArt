from tkinter import *
import random

# Draws Tkinter window
window = Tk()
window.title("Random Art")
window.resizable(0, 0)
window.configure(background="white")
window.geometry("450x500")

# Draws Tkinter canvas
canvas = Canvas(window, height=450, width=500, bg="white")
canvas.pack()

def shape():  # Function for generating the shape

    canvas.delete("all")  # Deletes previous art

    layers = random.randint(1, 10)  # Chooses a random number of polygons to generate
    new = 0

    while new != layers:
        pointnum = random.randint(1, 100) * 2
        points = random.sample(range(1, 450), pointnum)
        colors = ["red", "blue", "orange", "black", "violet", "green", "yellow", "white"]

        canvas.create_polygon(points, outline=random.choice(colors), fill=random.choice(colors))

        new += 1

genbutt = Button(window, text="Generate", bg="white", fg="black", font="arial 15 bold", command=shape)
genbutt.pack(pady=10)

window.mainloop()