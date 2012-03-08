""" A representation of a checker board
Ben Hartman 3/4/2012
"""

import random #For random generation functions
import itertools #For sweet fast list functions
import math #For the e constant

class board():
	""" Represents one checker board
	"""

	def __init__(self):
		"""Creates a starter board"""
		self.location = list("bbbbbbbbbbbb" + "eeeeeeee" + "rrrrrrrrrrrr")


	def randomBoard(self): #Generates a random board, NOTE: Will not be a valid board, just one with random stuff on it
		"""Generates a random board
		NOTE: The generated board may not be an actually valid board (one that could be actually played to)
		"""
		self.location = []
		choices = ['e', 'r', 'b', 'R', 'B']
		for x in xrange(32):
			self.location.append(random.choice(choices))
