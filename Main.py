import numpy as np
import tkinter as tk

SIZE = 100


def main(filda,fildb, fildcanvas,  step, canvas):
    step += 1
    drowfild(filda, fildcanvas)
    checkfild(filda, fildb)
    drowfild(fildb, fildcanvas)
    checkfild(fildb, filda)
    canvas.after(1, main(filda, fildb, fildcanvas, step, canvas))

def drowfild(fild, fildcanvas):
    for i in range(1, SIZE + 1):
        for j in range(1, SIZE + 1):
            if fild[i,j]:
                canvas.itemconfig(fildcanvas[i, j], fill="blue")
            else:
                canvas.itemconfig(fildcanvas[i, j], fill="white")
    canvas.update()


def checkfild(fild_old, fild_new):
    for i in range(1, SIZE):
        for j in range(1, SIZE):
            fild_new[i, j] = nextturn(fild_old, i, j)


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
        fildcanvas[i, j] = canvas.create_oval(i * 10 - 5, j * 10 - 5, i * 10 + 5, j * 10 + 5, outline="white")



filda[50, 51] = 1
filda[51, 51] = 1
filda[50, 50] = 1
filda[51, 50] = 1
filda[52, 49] = 1
filda[53, 51] = 1
filda[54, 51] = 1
filda[53, 50] = 1
filda[54, 50] = 1
step =1
main(filda, fildb, fildcanvas, step, canvas)

root.mainloop()