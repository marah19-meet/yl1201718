from turtle import *
import random
import math

class rectangle(Turtle):
	def __init__(self,height,speed,color,width):
		Turtle.__init__(self)
		self.shape("rectangle")
		self.shapesize(10)
		self.color(color)
		self.speed(speed)
		
 