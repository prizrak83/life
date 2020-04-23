import numpy as np
import tkinter as tk


SIZE = 100
FACTOR = 8


def main(filda, fildb, fildcanvas,  canvas):
    global step
    step += 1
    checkfild(filda, fildb, fildcanvas, canvas)
    root.title('Life' + '   ' + str(step))
    step += 1
    checkfild(fildb, filda, fildcanvas, canvas)
    root.title('Life' + '   ' + str(step))


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


def quit():
  global run, quit_flag
  if not(run):
    root.destroy()
  else:
    run = False
    quit_flag = True

def start_stop():
  global run, quit_flag ,start_flag
  run = not(run)
  if run:
    mainmenu.entryconfig(1, label='stop')
  else:
    mainmenu.entryconfig(1, label='start')

  while run:
    main(filda, fildb, fildcanvas, canvas)
  else:
    if quit_flag:
      root.destroy()


run = False
quit_flag = False
step =1
root = tk.Tk()
root.title('Life'+ '   ' + str(step))
canvas = tk.Canvas(root, width=SIZE*FACTOR, height=SIZE*FACTOR)
mainmenu=tk.Menu(root)

root.config(menu=mainmenu)
mainmenu.add_command(label='start', command=start_stop)
mainmenu.add_command(label='exit', command=quit)
root.protocol("WM_DELETE_WINDOW", quit)

canvas.pack()

filda = np.zeros((SIZE + 3, SIZE + 3), dtype=int)
fildb = np.zeros((SIZE + 3, SIZE + 3), dtype=int)
fildcanvas = np.zeros((SIZE+3, SIZE+3), dtype=int)

i, j = 1, 1
oval_size = FACTOR//2
for i in range(1, SIZE + 1):
    for j in range(1, SIZE + 1):
        fildcanvas[i, j] = canvas.create_oval(i * FACTOR - oval_size, j * FACTOR - oval_size,
                                              i * FACTOR + oval_size, j * FACTOR + oval_size,
                                              outline="white", fill = "white")

filda[49, 51] = 1
filda[49, 50] = 1
filda[50, 50] = 1
filda[51, 50] = 1
filda[50, 49] = 1
drowfild(filda, fildcanvas)
canvas.update()

root.mainloop()