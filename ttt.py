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

#scores = open("help.txt","r")
#help = scores.readlines()
#screen.addstr(3,55,help[0])
#screen.addstr(4,55,help[1])
#screen.addstr(5,55,help[2])
#screen.addstr(6,55,help[3])
#screen.addstr(7,55,help[4])
#screen.addstr(8,55,help[5])
#screen.addstr(9,55,help[6])
#screen.addstr(10,55,help[7])
#screen.addstr(11,55,help[8])
#screen.addstr(12,55,help[9])
#screen.addstr(13,55,help[10])
#screen.addstr(14,55,help[11])

row = 2
col = 8
player = 1

board = [[".",".","."],
	[".",".","."],
	[".",".","."]]

def nyerte():
	row1 = board[0][0]+board[0][1]+board[0][2]
	row2 = board[1][0]+board[1][1]+board[1][2]
	row3 = board[2][0]+board[2][1]+board[2][2]
	col1 = board[0][0]+board[1][0]+board[2][0]
	col2 = board[0][1]+board[1][1]+board[2][1]
	col3 = board[0][2]+board[1][2]+board[2][2]
	diag1 = board[0][0]+board[1][1]+board[2][2]
	diag2 = board[0][2]+board[1][1]+board[2][0]

	if row1 == 'XXX' or row2 == 'XXX' or row3 == 'XXX':
		return 'X-nyert'
	elif row1 == 'OOO' or row2 == 'OOO' or row3 == 'OOO':
		return 'O-nyert'
	elif col1 == 'XXX' or col2 == 'XXX' or col3 == 'XXX':
		return 'X-nyert'
	elif col1 == 'OOO' or col2 == 'OOO' or col3 == 'OOO':
		return 'O-nyert'
	elif diag1 == 'XXX' or diag2 == 'XXX':
		return 'X-nyert'
	elif diag1 == 'OOO' or diag2 == 'OOO':
		return 'O-nyert'
	else:
		return 'Döntetlen!'

try:
	while True:
		char = screen.getch()
		screen.addstr(13,22,"                     ")
		screen.addstr(13,22,nyerte())

		if char == ord('q'):
			break

		elif char == ord('r'):
			screen.addstr(0,0,map)
			board = [[".",".","."],
				[".",".","."],
				[".",".","."]]

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
				board[0][0] = 'X'
			elif row == 2 and col == 24:
				board[0][1] = 'X'
			elif row == 2 and col == 40:
				board[0][2] = 'X'
			elif row == 6 and col == 8:
				board[1][0] = 'X'
			elif row == 6 and col == 24:
				board[1][1] = 'X'
			elif row == 6 and col == 40:
				board[1][2] = 'X'
			elif row == 10 and col == 8:
				board[2][0] = 'X'
			elif row == 10 and col == 24:
				board[2][1] = 'X'
			elif row == 10 and col == 40:
				board[2][2] = 'X'

		elif char == 10 and player % 2 != 0:
			screen.addstr(row,col,'O')
			player += 1
			if row == 2 and col == 8:
				board[0][0] = 'O'
			elif row == 2 and col == 24:
				board[0][1] = 'O'
			elif row == 2 and col == 40:
				board[0][2] = 'O'
			elif row == 6 and col == 8:
				board[1][0] = 'O'
			elif row == 6 and col == 24:
				board[1][1] = 'O'
			elif row == 6 and col == 40:
				board[1][2] = 'O'
			elif row == 10 and col == 8:
				board[2][0] = 'O'
			elif row == 10 and col == 24:
				board[2][1] = 'O'
			elif row == 10 and col == 40:
				board[2][2] = 'O'

finally:
	curses.nocbreak(); screen.keypad(0); curses.echo()
	curses.endwin()
#----------------------------------------------------------
for i in range(3):
	for j in range(3):
		print(board[i][j])
	print()
