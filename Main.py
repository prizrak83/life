import numpy as np
import time
import tkinter as tk

SIZE = 100


def main(filda,fildb, fildcanvas,  step):
    step += 1
    drowfild(filda, fildcanvas)
    checkfild(filda, fildb)
    drowfild(fildb, fildcanvas)
    checkfild(fildb, filda)
    canvas.after(10,main(filda, fildb, fildcanvas, step))

def drowfild(fild, fildcanvas):
    for str in range(1, SIZE + 1):
        for s in range(1, SIZE + 1):
            if fild[str,s]:
                canvas.itemconfig(fildcanvas[str, s], fill="blue")
            else:
                canvas.itemconfig(fildcanvas[str, s], fill="white")
    canvas.update()


def checkfild(fild1, fild2):
    for str in range(1, SIZE):
        for s in range(1, SIZE):
            fild2[str, s] = nextturn(fild1, str, s)


def nextturn(fild, str, s):
    sosedi_kletki = sosedi(fild, str, s)
    if sosedi_kletki == 3 or ((sosedi_kletki == 2) and fild[str, s]):
        return 1
    return 0



def sosedi(fild, str, s):
    return (fild[str-1, s-1] + fild[str-1, s] + fild[str-1, s+1] + fild[str, s-1] + fild[str, s+1] +
            fild[str+1, s-1] + fild[str+1, s] + fild[str+1, s+1])


def printfild(fild):
    for str in range(1, SIZE + 1):

        for s in range(1, SIZE + 1):
            print(1 if fild[str, s] else 0, end=' ')
        print('')
    print(' ')


root = tk.Tk()
root.title = 'test'
canvas = tk.Canvas(root, width=SIZE*10, height=SIZE*10)
canvas.pack()



filda = np.zeros((SIZE + 3, SIZE + 3), dtype=int)
fildb = np.zeros((SIZE + 3, SIZE + 3), dtype=int)
fildcanvas = np.zeros((SIZE+3, SIZE+3), dtype=int)
str=1
s=1
for str in range(1, SIZE + 1):
    for s in range(1, SIZE + 1):
        fildcanvas[str, s] = canvas.create_oval(str * 10 - 5, s * 10 - 5, str * 10 + 5, s * 10 + 5, outline="white")



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
main(filda, fildb, fildcanvas, step)

root.mainloop()