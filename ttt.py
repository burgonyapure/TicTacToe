import sys

import curses
# get the curses screen window
screen = curses.initscr()
 
# turn off input echoing
curses.noecho()
 
# respond to keys immediately (don't wait for enter)
curses.cbreak()
 
# map arrow keys to special values
screen.keypad(True)
def move (y, x):
    print("\033[%d;%dH" % (y, x))

canvas = open("canvas.txt","r")
palya = canvas.read()
screen.addstr(palya)
try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_RIGHT:
            # print doesn't work with curses, use addstr instead
            screen.addstr(3, 9, 'right')
        elif char == curses.KEY_LEFT:
            screen.addstr(0, 0, 'left ')       
        elif char == curses.KEY_UP:
            screen.addstr(0, 0, 'up   ')       
        elif char == curses.KEY_DOWN:
            screen.addstr(0, 0, 'down ')
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
#----------------------------------------------------------
