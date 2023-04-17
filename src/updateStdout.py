from time import sleep, time
from colorama import Back, init as colorInit

for i in range(10):
    # sleep(0.1)
    # print(i, end="\r")
    sr = Back.BLUE+str(i)+Back.RESET + "   "+Back.CYAN+str(100+i)+Back.RESET
    print(sr,)

    # print(Back.CYAN, i+10, Back.RESET, end="\r")
sleep(1)
print('\033[10A',end='') # move cursor up 10 lines
print('\r',end='') # cursor back to start
print('\033[0J',end="") # erase from cursor to end
for i in range(10):
    # sleep(0.1)
    sr = Back.RED+str(i)+Back.RESET + "   "+Back.GREEN+str(100+i)+Back.RESET
    print(sr)
print("")
