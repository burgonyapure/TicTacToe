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

canvas = open("canvas.txt","r")
map = canvas.read()
screen.addstr(map)

row = 2
col = 8
player = 1

winner = [[0,1,2],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6],[3,4,5],[6,7,8]]

tomb = [[".",".","."],
	[".",".","."],
	[".",".","."]]

def nyerte():
	row1 = tomb[0]
try:
	while True:
		char = screen.getch()
		#screen.addstr(5,50,nyerte())
		nyerte()
		if char == ord('q'):
			break
		elif char == curses.KEY_RIGHT:
			col = col + 16
			if col > 40:
				col = 8
			screen.addstr(row, col, '')

		elif char == curses.KEY_LEFT:
			col = col - 16
			if col < 8:
				col = 40
			screen.addstr(row, col, '')

		elif char == curses.KEY_UP:
			row = row - 4
			if row < 2:
				row = 10
			screen.addstr(row, col, '')

		elif char == curses.KEY_DOWN:
			row = row + 4
			if row > 10:
				row = 2
			screen.addstr(row, col, '')

		elif char == 10 and player % 2 == 0:
			screen.addstr(row,col,'X')
			player += 1
			if row == 2 and col == 8:
				tomb[0][0] = 'X'
			elif row == 2 and col == 24:
				tomb[0][1] = 'X'
			elif row == 2 and col == 40:
				tomb[0][2] = 'X'
			elif row == 6 and col == 8:
				tomb[1][0] = 'X'
			elif row == 6 and col == 24:
				tomb[1][1] = 'X'
			elif row == 6 and col == 40:
				tomb[1][2] = 'X'
			elif row == 10 and col == 8:
				tomb[2][0] = 'X'
			elif row == 10 and col == 24:
				tomb[2][1] = 'X'
			elif row == 10 and col == 40:
				tomb[2][2] = 'X'

		elif char == 10 and player % 2 != 0:
			screen.addstr(row,col,'O')
			player += 1
			if row == 2 and col == 8:
				tomb[0][0] = 'O'
			elif row == 2 and col == 24:
				tomb[0][1] = 'O'
			elif row == 2 and col == 40:
				tomb[0][2] = 'O'
			elif row == 6 and col == 8:
				tomb[1][0] = 'O'
			elif row == 6 and col == 24:
				tomb[1][1] = 'O'
			elif row == 6 and col == 40:
				tomb[1][2] = 'O'
			elif row == 10 and col == 8:
				tomb[2][0] = 'O'
			elif row == 10 and col == 24:
				tomb[2][1] = 'O'
			elif row == 10 and col == 40:
				tomb[2][2] = 'O'

finally:
	curses.nocbreak(); screen.keypad(0); curses.echo()
	curses.endwin()
#----------------------------------------------------------
for i in range(3):
	for j in range(3):
		print(tomb[i][j])
	print()
