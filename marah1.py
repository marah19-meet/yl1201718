from turtle import *
import random
import math
colormode(255)
tracer(0)
hideturtle()
class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
		self.dx=dx
		self.dy=dy
		r=random.randint(0,255)
		g=random.randint(0,255)
		b=random.randint(0,255)
		self.color(r,g,b)

	def move(self,screen_width,screen_height):