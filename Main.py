import numpy as np
import tkinter as tk


SIZE = 100
FACTOR = 8


def main(filda, fildb, fildcanvas,  canvas):
    global step
    step += 1
    if np.array_equal(filda, fildb):
        stable()
        return
    checkfild(filda, fildb, fildcanvas, canvas)
    root.title('Life' + '   ' + str(step))
    step += 1
    if np.array_equal(filda, fildb):
        stable()
        return
    checkfild(fildb, filda, fildcanvas, canvas)
    root.title('Life' + '   ' + str(step))


def stable():
    global run
    run = False
    mainmenu.entryconfig(1, label='start')


def drowfild(fild, fildcanvas):
    global canvas
    for i in range(0, SIZE):
        for j in range(0, SIZE):
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
    global step
    if alive:
        return ("#%02X%02X%02X" % (0, ((step//25)%255), (step%255)))
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
  global run, quit_flag
  run = not(run)
  if run:
    mainmenu.entryconfig(1, label='stop')
  else:
    mainmenu.entryconfig(1, label='start')
  canvas.update()
  while run:
    main(filda, fildb, fildcanvas, canvas)
  else:
    if quit_flag:
      root.destroy()


def edit_fild(event):
  if not(run):
    i = event.x // FACTOR
    j = event.y // FACTOR
    if filda[i, j]:
      filda[i , j] = 0
      canvas.itemconfig(fildcanvas[i, j], fill='white')
    else:
      filda[i, j] = 1
      canvas.itemconfig(fildcanvas[i, j], fill='blue')


def clear():
    global filda, fildb,  run, step
    run = False
    step = 1
    root.title('Life' + '   ' + str(step))
    mainmenu.entryconfig(1, label='start')
    filda = np.zeros((SIZE + 2, SIZE + 2), dtype=int)
    fildb = np.zeros((SIZE + 2, SIZE + 2), dtype=int)
    for i in range(0, SIZE):
        for j in range(0, SIZE):
            canvas.itemconfig(fildcanvas[i, j], fill='white')
    drowfild(filda, fildcanvas)


def bomb():
    clear()
    filda[48, 50] = 1
    filda[49, 50] = 1
    filda[48, 51] = 1
    filda[49, 51] = 1
    filda[50, 49] = 1
    filda[51, 50] = 1
    filda[52, 50] = 1
    filda[51, 51] = 1
    filda[52, 51] = 1
    drowfild(filda, fildcanvas)


def r_pentomino():
    clear()
    filda[49, 51] = 1
    filda[49, 50] = 1
    filda[50, 50] = 1
    filda[51, 50] = 1
    filda[50, 49] = 1
    drowfild(filda, fildcanvas)


run = False
quit_flag = False
step = 1

root = tk.Tk()
root.title('Life'+ '   ' + str(step))
canvas = tk.Canvas(root, width=SIZE*FACTOR, height=SIZE*FACTOR)

mainmenu = tk.Menu(root)
root.config(menu=mainmenu)
fild_menu = tk.Menu(mainmenu, tearoff=0)
fild_menu.add_command(label='Clear', command=clear)
fild_menu.add_command(label='Bomb', command=bomb)
fild_menu.add_command(label='R-pentomino', command=r_pentomino)

mainmenu.add_command(label='start', command=start_stop)
mainmenu.add_cascade(label='fild', menu=fild_menu)
mainmenu.add_command(label='exit', command=quit)

root.protocol("WM_DELETE_WINDOW", quit)
root.bind('<Button-1>', edit_fild)
canvas.pack()

filda = np.zeros((SIZE + 2, SIZE + 2), dtype=int)
fildb = np.zeros((SIZE + 2, SIZE + 2), dtype=int)
fildcanvas = np.zeros((SIZE, SIZE), dtype=int)

i, j = 1, 1
oval_size = FACTOR//2
for i in range(0, SIZE):
    for j in range(0, SIZE):
        fildcanvas[i, j] = canvas.create_oval(i * FACTOR - oval_size, j * FACTOR - oval_size,
                                              i * FACTOR + oval_size, j * FACTOR + oval_size,
                                              outline="white", fill="white")

filda[49, 51] = 1
filda[49, 50] = 1
filda[50, 50] = 1
filda[51, 50] = 1
filda[50, 49] = 1

drowfild(filda, fildcanvas)
canvas.update()

root.mainloop()