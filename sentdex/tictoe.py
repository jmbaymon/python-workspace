game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
def win(current_game):
	for row in game:
		print(row)
		check.append(row[0])
		# horzionatal winner
		if row.count(row[0]) == len(row) and row[0] != 0:
			print("Winner!")



def game_board(game_map,player=0,row=0, column=0,just_display=False):
	try:
		print("   0  1  2")
		if not just_display:
			game_map[row][column] = player
		# display tictoe board
		for count, row in enumerate(game):
			print(count, row)
		return game_map
	except IndexError as e:
		print("Error: make sure you input row/column as 0, 1, or 2", e)
	except Exception as e:
		print("Something Really Bad happened", e)
game = game_board(game,just_display=True)
# game = game_board(game,player=1,row=3,column=1) #Error  
game = game_board(game,player=2,row=1,column=0)
# game = game_board(game_board,player=1,row=2,column=1)# Error

win(game)