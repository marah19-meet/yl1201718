from turtle import *
 #import random
# colormode(255)
class Rectangle(Turtle):
	def __init__(self,width,height):
		Turtle.__init__(self)
		register_shape("rectangle",((0,0),(0,height),(width,height),(width,0),(0,0)))
		self.shape("rectangle")
		self.setheading(90)
class Square(Turtle):
	def __init__(self,size):
		Rectangle.__init__(self,size,size)
	def random_color(self):
		r=random.randint(0,255)
		g=random.randint(0,255)
		b=random.randint(0,255)
		self.color(r,g,b)
square10=Square(50)
# rect1= Rectangle(50,50)

# 		self.shapesize(shapesize)
# 		self.shape("square")

# square1=Square(10)
# square1.random_color()
# 0
# class Rectangle(Turtle):
# 	def __init__(self,width,height):
# 		Turtle.__init__(self)
# 		register_shape("rectangle",((0,0),(0,height),(width,height),(width,0),(0,0)))
# 		self.shape("rectangle")
# 		self.setheading(90)	
# rect1= Rectangle(50,100)

mainloop()










# turtle.register_shape("Hexagone",((0,0),(30,-20),(0,-70),(-30,-50),(-30,-20),(0,0)))
# turtle.shape("Hexagone")
# turtle.mainloop()
# class Hexagon(Turtle):
# 	def __init__(self,shapesize):
# 		Turtle.__init__(self)
# 		self.shapesize(shapesize)
# 		self.shape("Hexagone")


