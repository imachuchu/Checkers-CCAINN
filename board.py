""" A representation of a checker board
Ben Hartman 3/4/2012
"""

import random #For random generation functions
import itertools #For sweet fast list functions
import math #For the e constant
import copy

class board():
	""" Represents one checker board
	"""

	def __init__(self):
		"""Creates a starter board
		
		The board is counted from 0 in the upper right, with black on top, and each movable square represented by a character
		"""
		self.location = list("bbbbbbbbbbbb" + "eeeeeeee" + "rrrrrrrrrrrr")

	def randomBoard(self):
		"""Generates a random board
		NOTE: The generated board may not be an actually valid board (one that could be actually played to)
		"""
		choices = ['e', 'r', 'b', 'R', 'B']
		self.location = [random.choice(choices) for x in range(32)]

	def genMoves(self,color,jumpFound=False): # !NOTE: Only works for black currently!
		"""Returns a set of future boards generatable from the current board. If none returns an empty set"""
		jumpBoards = set({})
		for square,location in zip(self.location,range(32)):
			if spot is not ('e' or 'r') and location <= 24: # So we can go down-left and down-right
				if (location % 4 is not 0) and (self.location[location+7] is 'e'): #Down-left jump
					if location % 8 < 4: #Odd numbered row
						if self.location[location+4] is ('r' or 'R'):
							newBoard = copy.copy(self)
							tempSet = newBoard.genMoves(color, jumpFound=True)
							if tempSet:
								jumpBoards = board | tempSet
							else:
								jumpBoards.add(newBoard)
					else:
						if self.location[location+3] is ('r' or 'R'):
							newBoard = copy.copy(self)
							tempSet = newBoard.genMoves(color, jumpFound=True)
							if tempSet:
								jum[Boards = board | tempSet
							else:
								jumpBoards.add(newBoard)
				if (location % 4 is not 3) and (self.location[location+9] is 'e'): #Down-right jump
					if location % 8 < 4: #Odd numbered row
						if self.location[location+5] is ('r' or 'R'):
							newBoard = copy.copy(self)
							tempSet = newBoard.genMoves(color, jumpFound=True)
							if tempSet:
								jumpBoards = board | tempSet
							else:
								jumpBoards.add(newBoard)
						if self.location[location+4] is ('r' or 'R'):
							newBoard = copy.copy(self)
							tempSet = newBoard.genMoves(color, jumpFound=True)
							if tempSet:
								jumpBoards = board | tempSet
							else:
								jumpBoards.add(newBoard)

			if spot is not ('e' or 'b') and location >= 9: # So we can go up-left and up-right
				if (location % 4 is not 0) and (self.location[location-7] is 'e'): #Up-left jump
					if location % 8 < 4: #Odd numbered row
						if self.location[location-4] is ('r' or 'R'):
							newBoard = copy.copy(self)
							tempSet = newBoard.genMoves(color, jumpFound=True)
							if tempSet:
								jumpBoards = board | tempSet
							else:
								jumpBoards.add(newBoard)
					else:
						if self.location[location-5] is ('r' or 'R'):
							newBoard = copy.copy(self)
							tempSet = newBoard.genMoves(color, jumpFound=True)
							if tempSet:
								jumpBoards = board | tempSet
							else:
								jumpBoards.add(newBoard)
				if (location % 4 is not 3) and (self.location[location-9] is 'e'): #Up-right jump
					if location % 8 < 4: #Odd numbered row
						if self.location[location-3] is ('r' or 'R'):
							newBoard = copy.copy(self)
							tempSet = newBoard.genMoves(color, jumpFound=True)
							if tempSet:
								jumpBoards = board | tempSet
							else:
								jumpBoards.add(newBoard)
						if self.location[location-4] is ('r' or 'R'):
							newBoard = copy.copy(self)
							tempSet = newBoard.genMoves(color, jumpFound=True)
							if tempSet:
								jumpBoards = board | tempSet
							else:
								jumpBoards.add(newBoard)
		if jumpBoards or jumpFound: #We've found at least one jump
			return jumpBoards

