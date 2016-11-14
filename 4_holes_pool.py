from Tkinter import *
import time

WIDTH = input("Enter width size (will be x100) ")*100
HEIGHT = input("Enter height size (will be x100) ")*100

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()
holes =[]
holes.append(canvas.create_oval(-25, -25, 25, 25, fill="black"))
holes.append(canvas.create_oval(WIDTH-25, -25, WIDTH+25, 25, fill="black"))
holes.append(canvas.create_oval(-25, HEIGHT-25, 25, HEIGHT+25, fill="black"))
holes.append(canvas.create_oval(WIDTH-25, HEIGHT-25, WIDTH+25, HEIGHT+25, fill="black"))
ball = canvas.create_oval(0, 0, 25, 25, fill="lightsteelblue", activefill="orange")
text = canvas.create_text(WIDTH/2, HEIGHT/2, anchor=CENTER, font=("Purisa", 20))
xspeed = 1.02
yspeed = 1

while True:
    canvas.move(ball, xspeed, yspeed)
    pos = canvas.coords(ball)
    posText = "POS["+str(int(pos[0]))+", "+str(int(pos[1]))+", "+str(int(pos[2]))+", "+str(int(pos[3]))+"]"
    canvas.itemconfig(text, text=posText)    
    if pos[3] >= HEIGHT+1 or pos[1] <= -1:
        yspeed = -yspeed
        time.sleep(5)
    elif pos[2] >= WIDTH+1 or pos[0] <= -1:
        xspeed = -xspeed
        time.sleep(5)
    tk.update()
    time.sleep(0.01)

        
tk.mainloop()
