""" A representation of a checker board
Ben Hartman 3/4/2012
"""

import random #For random generation functions
import itertools #For sweet fast list functions
import math #For the e constant

class board():

	def randomBoard(self): #Generates a random board, NOTE: Will not be a valid board, just one with random stuff on it
		self.location = []
		choices = ['e', 'r', 'b', 'R', 'B']
		for x in xrange(32):
			self.location.append(random.choice(choices))

class neuralNode(): # A node consists of some weights by which it listens to the previous layer

	def __init__(self,number=1, inweights=0): #Generates a node with random weights to a number of previous nodes
		weights = []
		self.weights = []
		if inweights != 0:
			self.weights = inweights 
			return
		for link in range(number):
			self.weights.append(random.uniform(-1,1))

	def evaluateLayer(self, layer): #Returns how much this node likes the input layer
		likeness = 0
		for piece in itertools.izip(self.weights, layer):
			likeness += piece[0] + piece[1]
		return likeness

	def evolveNode(self): # Returns a child note evolved off of this one
		futureWeights = []
		for node in self.weights:
			futureWeights.append(node+random.gauss(0,.2)) #May need to find a better standard deviation for this/or scale it
			#futureWeights.append(1/(1+math.pow(math.e,(-SCALINGFACTOR*node))))
		return neuralNode(inweights=futureWeights)
