import numpy as np

FILDH = 10
FILDW = 10

def main():
    printfild(filda)


def printfild(fild):
    for str in range(FILDW):

        for s in range(FILDH):
            print(1 if fild[str ,s]else 0, end = ' ')
        print('')

fildb = filda = np.zeros((FILDW, FILDH), dtype = bool)
filda[0, 5] = True

main()