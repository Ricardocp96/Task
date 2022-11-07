from asciimatics.screen import Screen
from time import sleep

#initialize open and closed door variables 
open = "O"
closed = "C"

def hundredDoors(screen):
    doors = [False] * 100
    for i in range(100):
        for j in range(i, 100, i+1):
            doors[j] = not doors[j]
            l=0
            p=j
            if j>=50:
                l = 1
                p=j-50
            if doors[j]:
                screen.print_at(open,p,l)
            else:
                screen.print_at(closed,p,l)
            screen.refresh()
            sleep(0.01) # Slow down there python
            
    
    j=3
    for i in range(100):
        if doors[i] == True:
            screen.print_at(i+1,0,j)
            j+=1
        screen.refresh()
    sleep(100) #don't close for 100 seconds

Screen.wrapper(hundredDoors)