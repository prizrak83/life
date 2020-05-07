import numpy as np
import tkinter as tk


SIZE = 100
FACTOR = 8


def main(fielda, fieldb, fieldcanvas,  canvas):
    global step
    step += 1
    if np.array_equal(fielda, fieldb):
        stable()
        return
    checkfield(fielda, fieldb, fieldcanvas, canvas)
    root.title('Life' + '   ' + str(step))
    step += 1
    if np.array_equal(fielda, fieldb):
        stable()
        return
    checkfield(fieldb, fielda, fieldcanvas, canvas)
    root.title('Life' + '   ' + str(step))


def stable():
    global run
    run = False
    mainmenu.entryconfig(1, label='start')


def drowfield(field, fieldcanvas):
    global canvas
    for i in range(0, SIZE):
        for j in range(0, SIZE):
            if field[i,j]:
                canvas.itemconfig(fieldcanvas[i, j], fill="blue")
            else:
                canvas.itemconfig(fieldcanvas[i, j], fill="white")
    canvas.update()


def checkfield(field_old, field_new, fieldcanvas, canvas):
    for i in range(1, SIZE):
        for j in range(1, SIZE):
            field_new[i, j] = nextturn(field_old, i, j)
            if field_new[i,j] != field_old[i,j]:
                canvas.itemconfig(fieldcanvas[i, j], fill=color(field_new[i,j]))
    canvas.update()


def color(alive):
    global step
    if alive:
        return ("#%02X%02X%02X" % (0, ((step//25)%255), (step%255)))
    return "white"


def nextturn(field, i, j):
    neighbours = neighbour(field, i, j)
    if neighbours == 3 or ((neighbours == 2) and field[i, j]):
        return 1
    return 0


def neighbour(field, i, j):
    return (field[i-1, j-1] + field[i-1, j] + field[i - 1, j + 1] + field[i, j - 1] + field[i, j + 1] +
            field[i + 1, j - 1] + field[i + 1, j] + field[i + 1, j + 1])


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
    main(fielda, fieldb, fieldcanvas, canvas)
  else:
    if quit_flag:
      root.destroy()


def edit_field(event):
  if not(run):
    i = event.x // FACTOR
    j = event.y // FACTOR
    if fielda[i, j]:
      fielda[i , j] = 0
      canvas.itemconfig(fieldcanvas[i, j], fill='white')
    else:
      fielda[i, j] = 1
      canvas.itemconfig(fieldcanvas[i, j], fill='blue')


def clear():
    global fielda, fieldb,  run, step
    run = False
    step = 1
    root.title('Life' + '   ' + str(step))
    mainmenu.entryconfig(1, label='start')
    fielda = np.zeros((SIZE + 2, SIZE + 2), dtype=int)
    fieldb = np.zeros((SIZE + 2, SIZE + 2), dtype=int)
    for i in range(0, SIZE):
        for j in range(0, SIZE):
            canvas.itemconfig(fieldcanvas[i, j], fill='white')
    drowfield(fielda, fieldcanvas)


def bomb():
    clear()
    fielda[48, 50] = 1
    fielda[49, 50] = 1
    fielda[48, 51] = 1
    fielda[49, 51] = 1
    fielda[50, 49] = 1
    fielda[51, 50] = 1
    fielda[52, 50] = 1
    fielda[51, 51] = 1
    fielda[52, 51] = 1
    drowfield(fielda, fieldcanvas)


def r_pentomino():
    clear()
    fielda[49, 51] = 1
    fielda[49, 50] = 1
    fielda[50, 50] = 1
    fielda[51, 50] = 1
    fielda[50, 49] = 1
    drowfield(fielda, fieldcanvas)


run = False
quit_flag = False
step = 1

root = tk.Tk()
root.title('Life'+ '   ' + str(step))
canvas = tk.Canvas(root, width=SIZE*FACTOR, height=SIZE*FACTOR)

mainmenu = tk.Menu(root)
root.config(menu=mainmenu)
field_menu = tk.Menu(mainmenu, tearoff=0)
field_menu.add_command(label='Clear', command=clear)
field_menu.add_command(label='Bomb', command=bomb)
field_menu.add_command(label='R-pentomino', command=r_pentomino)

mainmenu.add_command(label='start', command=start_stop)
mainmenu.add_cascade(label='field', menu=field_menu)
mainmenu.add_command(label='exit', command=quit)

root.protocol("WM_DELETE_WINDOW", quit)
root.bind('<Button-1>', edit_field)
canvas.pack()

fielda = np.zeros((SIZE + 2, SIZE + 2), dtype=int)
fieldb = np.zeros((SIZE + 2, SIZE + 2), dtype=int)
fieldcanvas = np.zeros((SIZE, SIZE), dtype=int)

i, j = 1, 1
oval_size = FACTOR//2
for i in range(0, SIZE):
    for j in range(0, SIZE):
        fieldcanvas[i, j] = canvas.create_oval(i * FACTOR - oval_size, j * FACTOR - oval_size,
                                              i * FACTOR + oval_size, j * FACTOR + oval_size,
                                              outline="white", fill="white")

fielda[49, 51] = 1
fielda[49, 50] = 1
fielda[50, 50] = 1
fielda[51, 50] = 1
fielda[50, 49] = 1

drowfield(fielda, fieldcanvas)
canvas.update()

root.mainloop()