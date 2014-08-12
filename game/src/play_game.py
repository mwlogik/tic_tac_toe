#! /usr/bin/python

"""
play_game.py -- Contains the functionality for representing the state
of the game and for handling the user's interactions with the game.

It's recommended that you read computer_moves.py first to understand
how the game board is represented.
"""

# Standard Python Libraries
# 
import time

# Game libraries
#
import computer_moves as comp


# Game Class -- representation of the game
#
class Game():
 def __init__(self, players):
  """
  Sets up the game.
  """
  
  self.gameboard = comp.createEmptyBoard()
  self.players = players
 
 def isValidMove(self, pos):
  """
  Check whether the user made a valid move.
  If he did, then update the board accordingly. Otherwise,
  let the user know what his error was.
  """
  
  board = self.gameboard
  
  #Make sure the player entered a valid position
  if(pos.isdigit()):
   pos = int(pos)
   if(pos > 9 or pos < 1):
    print "The position you entered is out of range."
    return False
  else:
   print "You must enter an integer between 1 to 9."
   return False
  
  #Make sure the player isn't placing a piece on a board position
  #where there's already a piece. If the move is valid, place the
  #piece on the board.
  
  pos = int(pos)
  pos_count = 0
  for row in range(3):
   for column in range(3):
    if(pos_count == pos-1):
     if(board[row][column] == 'e'):
	  board[row][column] = 'h'
	  return True
     else:
	  print "There is already a piece at that position."
	  return False
    else:
	  pos_count = pos_count+1
 
 def registerComputerMove(self):
  """
  The computer chooses its move and the board is updated accordingly.
  """
  self.gameboard = comp.minimaxDecision(self.gameboard)
  
 def isGameOver(self):
  board = self.gameboard
  if(comp.getUtility(board) == 1):
   print "Sorry, you lose."
   return True
  elif(comp.getUtility(board) == -1):
   print "Congratulations, you win!"
   return True
  elif(comp.getUtility(board) == 0):
   print "The game ends in a draw."
   return True
  else:
   return False
  
 def drawBoard(self):
  """
  Draws the board according to the current state of the game.
  """
  
  board = self.gameboard
  
  print ' _ _ _'
  
  for row in range(3):
   display = "|"
   for column in range(3):
    if(not board[row][column] == 'e'):
	 display = display + self.players[board[row][column]] + "|"
    else: display = display + " " + "|"
   print display
   print "|_|_|_|"

if __name__ == '__main__':
 """
 This handles the interactions between the user and the computer.
 """
 #Have the player choose his piece
 player_char = 'e'
 while(True):
  print ""
  input = raw_input('Please enter an x or an o depending on which player you want to be: ')
  if((not input == 'x') and (not input == 'o')):
   print "The character you entered was not an x or an o."
  else:
   player_char = input
   break
 
 #Assign the player and the computer their appropriate pieces.
 players = {}
 if(player_char == 'x'):
  players['h'] = 'x'
  players['c'] = 'o'
 else:
  players['h'] = 'o'
  players['c'] = 'x'

 #Start the game.
 game = Game(players)
 
 #Play the game
 while(True):
  game.drawBoard()
  if(game.isGameOver()):
   break
  else:
   print""
   pos = raw_input("Please enter the position of the board where you'd like to place your piece: ")
   if(game.isValidMove(pos)):
    if(game.isGameOver()):
	 game.drawBoard()
	 break
    else:
     game.drawBoard()
     print ""
     print "Thinking..."
     game.registerComputerMove()
     time.sleep(4)
	 
	 
  