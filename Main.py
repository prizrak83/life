import numpy as np
import tkinter as tk

SIZE = 100


def main(filda,fildb, fildcanvas,  step, canvas):
    step += 1
#    drowfild(filda, fildcanvas)
    checkfild(filda, fildb, fildcanvas, canvas)
#    drowfild(fildb, fildcanvas)
    checkfild(fildb, filda, fildcanvas, canvas)
    canvas.after(1, main(filda, fildb, fildcanvas, step, canvas))

def drowfild(fild, fildcanvas):
    for i in range(1, SIZE + 1):
        for j in range(1, SIZE + 1):
            if fild[i,j]:
                canvas.itemconfig(fildcanvas[i, j], fill="blue")
            else:
                canvas.itemconfig(fildcanvas[i, j], fill="white")
    canvas.update()


def checkfild(fild_old, fild_new, fildcanvas, canvas):
    for i in range(1, SIZE):
        for j in range(1, SIZE):
            fild_new[i, j] = nextturn(fild_old, i, j)
            if fild_new[i,j] != fild_old[i,j]:
                canvas.itemconfig(fildcanvas[i, j], fill=color(fild_new[i,j]))
    canvas.update()

def color(alive):
    if alive:
        return "blue"
    return "white"


def nextturn(fild, i, j):
    neighbours = neighbour(fild, i, j)
    if neighbours == 3 or ((neighbours == 2) and fild[i, j]):
        return 1
    return 0



def neighbour(fild, i, j):
    return (fild[i-1, j-1] + fild[i-1, j] + fild[i - 1, j + 1] + fild[i, j - 1] + fild[i, j + 1] +
            fild[i + 1, j - 1] + fild[i + 1, j] + fild[i + 1, j + 1])



root = tk.Tk()
root.title = 'test'
canvas = tk.Canvas(root, width=SIZE*10, height=SIZE*10)
canvas.pack()



filda = np.zeros((SIZE + 3, SIZE + 3), dtype=int)
fildb = np.zeros((SIZE + 3, SIZE + 3), dtype=int)
fildcanvas = np.zeros((SIZE+3, SIZE+3), dtype=int)

i, j = 1, 1
for i in range(1, SIZE + 1):
    for j in range(1, SIZE + 1):
        fildcanvas[i, j] = canvas.create_oval(i * 10 - 5, j * 10 - 5, i * 10 + 5, j * 10 + 5,
                                              outline="white", fill = "white")

canvas.update()


filda[49, 51] = 1
filda[49, 50] = 1
filda[50, 50] = 1
filda[51, 50] = 1
filda[50, 49] = 1
drowfild(filda, fildcanvas)
canvas.update()
step =1
main(filda, fildb, fildcanvas, step, canvas)

root.mainloop()