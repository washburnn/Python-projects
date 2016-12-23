import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.font import *
from tkinter import filedialog
from PIL import Image, ImageDraw

WIDTH = 876
HEIGHT = 500
BG_COLOR = "black"
TC = "white"
RAD = 10
BGC = 0

a = [0 for i in range(11)]
a[0] = "yellow"
a[1] = "pink"
a[2] = "blue"
a[3] = "white"
a[4] = "magenta"
a[5] = "grey"
a[6] = "brown"
a[7] = "orange"
a[8] = "gold"
a[9] = "black"
a[10] = "green"


def mmove(event):
    cv.create_oval(event.x - RAD, event.y - RAD, event.x + RAD, event.y + RAD, fill=TC, outline="")
    draw.ellipse([event.x - RAD, event.y - RAD, event.x + RAD, event.y + RAD], TC, TC)



def change_color(event):
    cv.create_oval(event.x - RAD, event.y - RAD, event.x + RAD, event.y + RAD, fill=TC, outline="")
    draw.ellipse([event.x - RAD, event.y - RAD, event.x + RAD, event.y + RAD], TC, TC)


def change_bg(event):
    global BGC
    BGC = (BGC + 1) % 2
    if BGC == 1:
        cv["bg"] = 'white'
    elif BGC == 0:
        cv["bg"] = 'black'


def bC(color):
    global TC
    TC = color


def cSize(opt):
    global RAD
    if opt == 0 and RAD < 40:
        RAD += 5
    elif opt == 1 and RAD > 0:
        RAD -= 5


def menu():
    global a
    t = "\t   "
    s = 'left'
    Button(text=t, bg=a[0], command=lambda: bC(a[0])).pack(side=s)
    Button(text=t, bg=a[1], command=lambda: bC(a[1])).pack(side=s)
    Button(text=t, bg=a[2], command=lambda: bC(a[2])).pack(side=s)
    Button(text=t, bg=a[3], command=lambda: bC(a[3])).pack(side=s)
    Button(text=t, bg=a[4], command=lambda: bC(a[4])).pack(side=s)
    Button(text=t, bg=a[5], command=lambda: bC(a[5])).pack(side=s)
    Button(text=t, bg=a[6], command=lambda: bC(a[6])).pack(side=s)
    Button(text=t, bg=a[7], command=lambda: bC(a[7])).pack(side=s)
    Button(text=t, bg=a[8], command=lambda: bC(a[8])).pack(side=s)
    Button(text=t, bg=a[9], command=lambda: bC(a[9])).pack(side=s)
    Button(text=t, bg=a[10], command=lambda: bC(a[10])).pack(side=s)
    Button(text='\t+\t', bg='grey', command=lambda: cSize(0)).pack(side=s)
    Button(text='\t-\t', bg='grey', command=lambda: cSize(1)).pack(side=s)


def save_as():
    f = filedialog.asksaveasfilename(
        defaultextension=".jpg",
        filetypes=(("jpeg", "*.jpg"), ("jpeg", "*.jpeg")))
    if f:
        image1.save(f)


def save(event):
    f = filedialog.asksaveasfilename(
        defaultextension=".jpg",
        filetypes=(("jpeg", "*.jpg"), ("jpeg", "*.jpeg")))
    if f:
        image1.save(f)


def close_win():
    root.destroy()


def exit(event):
    root.destroy()


def new_file():
    cv.delete("all")



root = tkinter.Tk()
root.resizable(False, False)
text = tkinter.Text(root)
root.title("PytPaint")

cv = Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
cv.pack()

menu()

m = Menu(root)
root.config(menu=m)
fm = Menu(m)
m.add_cascade(label="File", menu=fm)
fm.add_command(label="New", command=new_file)
fm.add_command(label="Save", command=save_as)
fm.add_command(label="Exit", command=close_win)

hm = Menu(m)
m.add_cascade(label="Help", menu=hm)
hm.add_command(label="About")

image1 = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
draw = ImageDraw.Draw(image1)

cv.bind('<Button-1>', change_color)
cv.bind('<Button-3>', change_bg)
cv.bind('<B1-Motion>', mmove)
root.bind('<Control-x>', exit)
root.bind('<Control-s>', save)

root.mainloop()
