from turtle import Turtle
import turtle
import random
import math
# RUNNING=True
# SLEEP=0.0077
# SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
# SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
turtle.hideturtle()
class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
		self.shape("circle")
		self.shapesize(r/10)
		self.r = r
		self.color(color)
		self.dx=dx
		self.dy=dy
		# r=random.randint(0,255)
		# g=random.randint(0,255)
		# b=random.randint(0,255)
		# self.color(r,g,b)

	def move(self,screen_width,screen_height):
		
		current_x=self.xcor()
		current_y=self.ycor()
		new_x=current_x+dx
		new_y=current_y+dy
		right_side_ball=new_x+r
		left_side_ball=new_x-r
		top_side_ball=new_y+r
		bottom_side_ball=new_y-r
		self.goto(new_x,new_y)



		if right_side_ball>screen_width:
			self.dx=-self.dx
		elif bottom_side_ball<-screen_height:
			self.dy=-self.dy
		elif left_side_ball<-screen_width:
			self.dx=-self.dx
		elif top_side_ball>screen_height:
			self.dy=-self.dy





		# def top(self):
		# 	return.self.ycor()+(0.5*self.height)
		# def bottom(self):
		# 	return.self.ycor()-(0.5*self.height)
		# def right(self):
		# 	return.self.xcor()+(o.5*self.width)
		# def left(self):
		# 	return.self.xcor()-(0.5*self.width)
		# if(A.top()>B.bottom()and A.right()>B.left()and A.bottom()<B.top()and A.left()>B.right()):

# my_ball=Ball(100,0,5,5,10,"red")
# my_ball.goto(10,10)
		

# turtle.mainloop()