from cProfile import label
from functools import partial
from tkinter import *
from tkinter import colorchooser
from turtle import left

root = Tk()
root.geometry("800x500")
root.title("Paint")
color = "black"
strokeSize = IntVar()
strokeSize.set(5)

def chooseColor(event):
    global color
    print(color)
    color = colorchooser.askcolor(title ="Asmit")
    color = color[1]
    print(color)
    

def changeColor(c):
    global color
    color = c

def paint(event):
    x = event.x
    y = event.y
    canvas.create_oval((x,y,x+strokeSize.get(),y+strokeSize.get()), fill=color, width=5, outline=color)

def clearAll():
  canvas.delete("all")

frameLeft = Frame(root, relief=SUNKEN, borderwidth=5, bg="grey")
frameLeft.pack(side="left", fill=Y)
frameRight = Frame(root, relief=SUNKEN, borderwidth=5, bg="grey")
frameRight.pack(side="left")
canvas = Canvas(frameRight, height=500, width=600, bg="white")
canvas.pack(side="left")
dashLabel = Label(frameLeft, text="Dashboard", width=13)
dashLabel.pack()
btnBlue = Button(frameLeft, text="Blue", bg="blue", command=partial(changeColor, "blue"), width=10)
btnBlue.pack()
btnGreen = Button(frameLeft, text="Green", bg="green", command=partial(changeColor, "green"), width=10)
btnGreen.pack()
btnRed = Button(frameLeft, text="Red", bg="red", command=partial(changeColor, "red"), width=10)
btnRed.pack()
btnYellow = Button(frameLeft, text="Eraser", bg="white", command=partial(changeColor, "white"), width=10)
btnYellow.pack()
btnEraseAll = Button(frameLeft, text="EraseAll", bg="white", command=clearAll, width=10)
btnEraseAll.pack()
btnChoose = Button(frameLeft, text="Choose Color")
btnChoose.pack()
btnChoose.bind("<Button-1>", chooseColor)

strokeLabel = Label(frameLeft, text="Select Stroke Size")
strokeLabel.pack()
scale = Scale(frameLeft, from_=1, to=15, variable=strokeSize, length=200)
scale.pack()
canvas.bind("<B1-Motion>", paint)


root.mainloop()