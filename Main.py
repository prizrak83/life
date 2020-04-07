import numpy as np

FILDH = 10
FILDW = 10

def main(filda,fildb):
    printfild(filda)
    checkfild(filda, fildb)
    printfild(fildb)


def checkfild(fild1, fild2):
    for str in range(1, FILDW):
        for s in range(1, FILDH):
            fild2[str, s] = nextturn(fild1, str, s)



def nextturn(fild, str, s):
    if sosedi(fild, str, s) == 3 or ((sosedi(fild, str, s) == 2) and fild[str, s]):
        return True
    return False

def sosedi(fild, str, s):
    return (int(fild[str-1, s-1])+int(fild[str-1, s])+int(fild[str-1, s+1])+
            int(fild[str, s-1])+int(fild[str, s+1])+
            int(fild[str+1, s-1])+int(fild[str+1, s])+int(fild[str+1, s+1]))

def printfild(fild):
    for str in range(1, FILDW+1):

        for s in range(1,FILDH+1):
            #print(1 if fild[str, s] else 0, sosedi(fild, str, s), sep='', end=' ')
            print(1 if fild[str, s] else 0, end=' ')
        print('')


filda = np.zeros((FILDW+3, FILDH+3), dtype = bool)
fildb = np.zeros((FILDW+3, FILDH+3), dtype = bool)
filda[5, 5] = True
filda[5, 6] = True
filda[5, 7] = True

main(filda,fildb)