import curses
import time
while True:
	kezd = input("ki kezdjen? (O vagy X)\n")
	if kezd == 'O' or kezd == 'o':
		player = 1
		break
	elif kezd == 'X' or kezd == 'x':
		player = 2
		break
	else:
		print("O vagy X lehet")
		continue
# curses ablak
screen = curses.initscr()
# szinek
curses.start_color()
curses.use_default_colors()
curses.init_pair(1,7,9)
curses.noecho()
# nem kell enterre várni
curses.cbreak()
# nyilak
screen.keypad(True)

canvas = open("canvas.txt","r")
map = canvas.read()
screen.addstr(map)
canvas.close()

#f_h = open("help.txt","r")
#help = f_h.readlines()
#f_h.close()
#for i in range(len(help)):
#	screen.addstr(i+1,55,help[i])

row = 2
col = 8
#xscore = 0
#oscore = 0
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
e = 0
try:
		
	while True:
		char = screen.getch()	
			
		if char == ord('q'):
			break
		elif char == ord('r'):
			screen.addstr(0,0,map)
			board = [[".",".","."],
				[".",".","."],
				[".",".","."]]
			row = 2
			col = 8
			e = 0
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
			e += 1
			if row == 2 and col == 8:
				if board[0][0] == '.':
					board[0][0] = 'X'
				else:
					screen.addstr(row,col,board[0][0])
					player -= 1
					e -= 1
			elif row == 2 and col == 24:
				if board[0][1] == '.':
					board[0][1] = 'X'
				else:
					screen.addstr(row,col,board[0][1])
					player -= 1
					e -= 1
			elif row == 2 and col == 40:
				if board[0][2] == '.':
					board[0][2] = 'X'
				else:
					screen.addstr(row,col,board[0][2])
					player -= 1
					e -= 1
			elif row == 6 and col == 8:
				if board[1][0] == '.':
					board[1][0] = 'X'
				else:
					screen.addstr(row,col,board[1][0])
					player -= 1
					e -= 1
			elif row == 6 and col == 24:
				if board[1][1] == '.':
					board[1][1] = 'X'
				else:
					screen.addstr(row,col,board[1][1])
					player -= 1
					e -= 1
			elif row == 6 and col == 40:
				if board[1][2] == '.':
					board[1][2] = 'X'
				else:
					screen.addstr(row,col,board[1][2])
					player -= 1
					e -= 1
			elif row == 10 and col == 8:
				if board[2][0] == '.':
					board[2][0] = 'X'
				else:
					screen.addstr(row,col,board[2][0])
					player -= 1
					e -= 1
			elif row == 10 and col == 24:
				if board[2][1] == '.':
					board[2][1] = 'X'
				else:
					screen.addstr(row,col,board[2][1])
					player -= 1
					e -= 1
			elif row == 10 and col == 40:
				if board[2][2] == '.':
					board[2][2] = 'X'
				else:
					screen.addstr(row,col,board[2][2])
					player -= 1
					e -= 1
			if nyerte() == "X-nyert" and nyerte() != "O-nyert":
				screen.addstr(13,22,"                     ")
				screen.addstr(13,22,nyerte(),curses.A_STANDOUT+curses.A_BLINK+curses.A_BOLD+curses.color_pair(1))
				screen.refresh()
				time.sleep(3)
				#xscore += 1
				#screen.addstr(11,59,str(xscore))
				break
			elif e == 9:
				screen.addstr(13,22,"                     ")
				screen.addstr(13,22,nyerte(),curses.A_STANDOUT+curses.A_BLINK+curses.A_BOLD+curses.color_pair(1))
				screen.refresh()
				time.sleep(3)
				break

		elif char == 10 and player % 2 != 0:
			screen.addstr(row,col,'O')
			player += 1
			e += 1
			if row == 2 and col == 8:
				if board[0][0] == '.':
					board[0][0] = 'O'
				else:
					screen.addstr(row,col,board[0][0])
					player -= 1
					e -= 1
			elif row == 2 and col == 24:
				if board[0][1] == '.':
					board[0][1] = 'O'
				else:
					screen.addstr(row,col,board[0][1])
					player -= 1
					e -= 1
			elif row == 2 and col == 40:
				if board[0][2] == '.':
					board[0][2] = 'O'
				else:
					screen.addstr(row,col,board[0][2])
					player -= 1
					e -= 1
			elif row == 6 and col == 8:
				if board[1][0] == '.':
					board[1][0] = 'O'
				else:
					screen.addstr(row,col,board[1][0])
					player -= 1
					e -= 1
			elif row == 6 and col == 24:
				if board[1][1] == '.':
					board[1][1] = 'O'
				else:
					screen.addstr(row,col,board[1][1])
					player -= 1
					e -= 1
			elif row == 6 and col == 40:
				if board[1][2] == '.':
					board[1][2] = 'O'
				else:
					screen.addstr(row,col,board[1][2])
					player -= 1
					e -= 1
			elif row == 10 and col == 8:
				if board[2][0] == '.':
					board[2][0] = 'O'
				else:
					screen.addstr(row,col,board[2][0])
					player -= 1
					e -= 1
			elif row == 10 and col == 24:
				if board[2][1] == '.':
					board[2][1] = 'O'
				else:
					screen.addstr(row,col,board[2][1])
					player -= 1
					e -= 1
			elif row == 10 and col == 40:
				if board[2][2] == '.':
					board[2][2] = 'O'
				else:
					screen.addstr(row,col,board[2][2])
					player -= 1
					e -= 1
			if nyerte() == "O-nyert" and nyerte() != "X-nyert":
				screen.addstr(13,22,"                     ")
				screen.addstr(13,22,nyerte(),curses.A_STANDOUT+curses.A_BLINK+curses.A_BOLD+curses.color_pair(1))
				screen.refresh()
				time.sleep(3)
				#oscore += 1
				break		
			elif e == 9:
				screen.addstr(13,22,"                     ")
				screen.addstr(13,22,nyerte(),curses.A_STANDOUT+curses.A_BLINK+curses.A_BOLD+curses.color_pair(1))
				screen.refresh()
				time.sleep(3)
				break
		
finally:
	curses.nocbreak(); screen.keypad(0); curses.echo()
	curses.endwin()
#----------------------------------------------------------
print("\t----DEBUG INFO----")
for i in range(3):
	for j in range(3):
		print("\t"+board[i][j],end='')
	print()
print("\t-------END--------")
#print("\n\t-----------------MEMORY INFO------------------")
#for i in range(3):
#	for j in range(3):
#		print("\t"+hex(id(board[i][j])),end='')
#	print()
#print("\t---------------------END----------------------")
#print(hex(id(kezd)))
