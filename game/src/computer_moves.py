"""
computer_moves.py -- Contains all the functionality to help
the computer determine the next move it should make.

The game-board is represented by a list of 3 lists where the nth member
of the list corresponds to the nth row of the game-board. Each of the
3 lists will have 3 characters where each character corresponds to the 
entry in the nth column of whichever row you're looking at.

The human player is represented on the game-board by an h, the
computer player by a c, and the character e corresponds to an
tile on the game-board that doesn't have a piece on it yet.

The functions maxValue, minValue and minimaxDecision correspond to
my implementations of the functions which are necessary to implement
the Minimax adversarial-search algorithm as outlined in the third 
edition of 'Artificial Intelligence: A modern approach' by 
Stuart Russell and Peter Norvig.
"""

def getWinningPositions():
 """
 Returns a list of every possible winning-board combination.
 """
 row_wins = [[(row,column) for column in range(3)] for row in range(3)]
 
 column_wins = [[(row,column) for row in range(3)] for column in range(3)]
 
 diagonal_wins = []
 diagonal_wins.append([(i,i) for i in range(3)])
 diagonal_wins.append([(i,2-i) for i in range(3)])
 
 return [win for win_type in [row_wins,column_wins,diagonal_wins] for win in win_type]

wins = getWinningPositions()

def createEmptyBoard():
 """
 Create a board where each position has an 'e'.
 """
 return [['e' for i in range(3)] for i in range(3)]

def getEmptyPositions(state):
 """
 Collect the board positions for which there is no piece on the board.
 """
 board_positions = [(i,j) for i in range(3) for j in range(3)]
 isEmpty = (lambda pos: state[pos[0]][pos[1]] == 'e')
 return filter(isEmpty, board_positions)
   
def getMoves(player,state):
 """
 Collect all the possible moves a player can make given the state of the game.
 """
 moves = []
 empties = getEmptyPositions(state)
 
 #Append each possible next move to moves
 for emptyPos in empties:
  resultState = createEmptyBoard()
  for row in range(3):
   for column in range(3):
    if((row,column) == emptyPos):
     resultState[row][column] = player
    else:
     resultState[row][column] = state[row][column]
  moves.append(resultState)
 
 return moves

def getUtility(state):
 """
 Calculates the computer player's utility i.e how beneficial 
 a state of the game is for the computer player.

 return:
     1: win for the computer
     0: draw
    -1: loss for the computer
    -2: undetermined utility
 """

 #Try to find a winner
 for win in wins:
  h_count = 0
  c_count = 0
  for pos in win:
   if(state[pos[0]][pos[1]] == 'h'):
    h_count = h_count + 1
   elif(state[pos[0]][pos[1]] == 'c'):
    c_count = c_count + 1
   else:
    pass
  if(h_count == 3):
   return -1
  elif(c_count == 3):
   return 1
  else:
   pass

 #If there's no winner, determine if the game ends in a draw 
 #or if we must keep searching.
 if('e' in [state[row][column] for row in range(3) for column in range(3)]):
  return -2
 else:
  return 0

def maxValue(state):
 """
 Compute the utility of the computer player's best possible
 move when the game is in the state under examination.
 """
 
 utility = getUtility(state)
 
 if(utility >= -1 and utility <= 1):
  return utility
 
 utility = -100
 
 for move in getMoves('c',state):
  utility = max(utility, minValue(move))
 
 return utility
 


def minValue(state):
 """
 Compute the utility of the human player's best possible
 move when the game is in the state under examination.
 """
 
 utility = getUtility(state)
 
 if(utility >= -1 and utility <= 1):
  return utility

 utility = 100
 
 for move in getMoves('h',state):
  utility = min(utility, maxValue(move))
 
 return utility


def minimaxDecision(state):
 """
 Find the best move for the computer to make.
 """

 computer_move = []
 utility = -2
 
 for move in getMoves('c',state):
  move_utility = minValue(move)
  
  if(move_utility > utility):
   computer_move = move
   utility = move_utility
 
 return computer_move 