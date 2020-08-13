torre1 = 1
torre2 = 2
torre3 = 3
n= 4
def hanoi(n, ini, des, aux):
    if n==1:
        print ("mueva el disco "+str(n)+" desde la torre "+str(ini)+" hasta la torre "+str(des))
    else:
        hanoi(n-1, ini, aux, des)
        print ("mueva el disco "+str(n)+" desde la torre "+str(ini)+" hasta la torre "+str(des))
        hanoi(n-1, aux, des, ini)
hanoi (n, torre1, torre3, torre2)