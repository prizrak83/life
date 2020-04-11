import numpy as np
import time

FILDH = 100
FILDW = 100

def main(filda,fildb):
    s = 500
    while s>0 :
#        printfild(filda)
        checkfild(filda, fildb)
#        printfild(fildb)
        checkfild(fildb, filda)
        s -= 1
#        print(s)
#    printfild(filda)


def checkfild(fild1, fild2):
    for str in range(1, FILDW):
        for s in range(1, FILDH):
            fild2[str, s] = nextturn(fild1, str, s)


def nextturn(fild, str, s):
    sosedi_kletki = sosedi(fild, str, s)
    if sosedi_kletki == 3 or ((sosedi_kletki == 2) and fild[str, s]):
        return True
    return False



def sosedi(fild, str, s):
    return (int(fild[str-1, s-1])+int(fild[str-1, s])+int(fild[str-1, s+1])+
            int(fild[str, s-1])+int(fild[str, s+1])+
            int(fild[str+1, s-1])+int(fild[str+1, s])+int(fild[str+1, s+1]))


def printfild(fild):
    for str in range(1, FILDW+1):

        for s in range(1,FILDH+1):
            print(1 if fild[str, s] else 0, end=' ')
        print('')
    print(' ')

start_time = time.process_time()
print(start_time)
filda = np.zeros((FILDW+3, FILDH+3), dtype=bool)
fildb = np.zeros((FILDW+3, FILDH+3), dtype=bool)

filda[3, 1] = True
filda[3, 2] = True
filda[3, 3] = True
filda[2, 3] = True
filda[1, 2] = True

filda[2, 7] = True
filda[2, 8] = True
filda[2, 9] = True

main(filda, fildb)
print(time.process_time() - start_time)