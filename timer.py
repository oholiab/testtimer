import sys
import time
import signal
import math
import tty
import os
from select import select
from threading import Thread

key = None
quit_all = False

def quit():
    global quit_all
    quit_all = True
    os.system('stty sane')
    sys.exit(0)

def input_loop():
    global key
    global quit_all
    if quit_all == True:
        quit()
    tty.setraw(sys.stdin)
    while True:
        dr,dw,de = select([sys.stdin], [], [], 0)
        if dr != []:
            key = sys.stdin.read(1)
            if key == 'q':
                quit()

def run(t):
    global key
    global quit_all
    Thread(target=input_loop).start()
    now = time.time()
    then = now + t
    left_last = 0
    while now < then:
        if quit_all == True:
            quit()
        left = then - now
        left_int = math.floor(left)
        if left_last != left_int:
            sys.stdout.write("\r" + str(left_int) + "               ")
        if key == 'a':
            sys.stdout.write("\rlololol")
        key = None
        left_last = left_int
        now = time.time()
    quit()


if __name__ == "__main__":
    run(30)
