from turtle import *
import turtle
import time
import random
from ball import Ball
#tracer(0)
#hideturtle()
RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2


my_ball=Ball(100,0,5,5,10,"red")
my_ball.goto(10,10)
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5	
BALLS=[]	
for i in range(NUMBER_OF_BALLS):

	x=random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
	y=random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
	dx=random.randint(int(MINIMUM_BALL_DX ),int (MAXIMUM_BALL_DX))
	dy=random.randint(int(MINIMUM_BALL_DY ),int (MAXIMUM_BALL_DY))
	r=random.randint(int(MINIMUM_BALL_RADIUS),int(MAXIMUM_BALL_RADIUS))
	color = (random.randint(0,255),random.randint(0,255), random.randint(0,255))

	NEW_BALL=Ball(x,y,dx,dy,r,color)
	BALLS.append(NEW_BALL)



def move_all_balls():
	for i in BALLS:
		i.move(SCREEN_WIDTH,SCREEN_HEIGHT)

move_all_balls()

def collide(ball_a,ball_b):
	if ball_a==ball_b:
		return False
	b1y=ball_a.ycor()
	b2y=ball_b.ycor()
	b1x=ball_a.xcor()
	b2x=ball_b.xcor()
	b1r=ball_a.r
	b2r=ball_b.r
	sr=b1r+b2r
	d=((b2x-b1x)**2+(b2y-b1y)**2)**0.5
	if d<=sr:
		return True
	else:
		return False
def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a,ball_b)== True:

				radius1=ball_a.r
				radius2=ball_b.r

				if radius1>radius2:
					ball_a.r=radius1+1

					x=random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
					y=random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
					dx=random.randint(int(MINIMUM_BALL_DX ),int (MAXIMUM_BALL_DX))
					dy=random.randint(int(MINIMUM_BALL_DY ),int (MAXIMUM_BALL_DY))
					r=random.randint(int(MINIMUM_BALL_RADIUS),int(MAXIMUM_BALL_RADIUS))
					color = (random.randint(0,255),random.randint(0,255), random.randint(0,255))

					while dx==0:
						dx=random.randint(int(MINIMUM_BALL_DX ),int (MAXIMUM_BALL_DX))
					while dy==0:
						dy=random.randint(int(MINIMUM_BALL_DY ),int (MAXIMUM_BALL_DY))


					ball_b.goto(x,y)
					ball_b.dx=dx
					ball_b.dy=dy
					ball_b.r=r
					ball_b.color(color)
					ball_b.shapesize(r/10)
					ball_a.shapesize(ball_a.r/10)

				if radius1<radius2:
					ball_b.r=radius2+1
					x=random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
					y=random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
					dx=random.randint(int(MINIMUM_BALL_DX ),int (MAXIMUM_BALL_DX))
					dy=random.randint(int(MINIMUM_BALL_DY ),int (MAXIMUM_BALL_DY))
					r=random.randint(int(MINIMUM_BALL_RADIUS),int(MAXIMUM_BALL_RADIUS))
					color = (random.randint(0,255),random.randint(0,255), random.randint(0,255))


					while dx==0:
						dx=random.randint(int(MINIMUM_BALL_DX ),int (MAXIMUM_BALL_DX))
					while dy==0:
						dy=random.randint(int(MINIMUM_BALL_DY ),int (MAXIMUM_BALL_DY))


					ball_a.goto(x,y)
					ball_a.dx=dx
					ball_a.dy=dy
					ball_a.r=r
					ball_a.color(color)
					ball_a.shapesize(r/10)
					ball_b.shapesize(ball_b.r/10)

check_all_balls_collision()


def check_myball_collision():
	for i in BALLS:
		if collide (my_ball,i)==True:
			radius1=my_ball.r
			radius2=i.r







			if radius1<radius2:
				return False
			else:
					my_ball.r=radius1+1
					x=random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
					y=random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
					dx=random.randint(int(MINIMUM_BALL_DX ),int (MAXIMUM_BALL_DX))
					dy=random.randint(int(MINIMUM_BALL_DY ),int (MAXIMUM_BALL_DY))
					r=random.randint(int(MINIMUM_BALL_RADIUS),int(MAXIMUM_BALL_RADIUS))
					color = (random.randint(0,255),random.randint(0,255), random.randint(0,255))


					while dx==0:
						dx=random.randint(int(MINIMUM_BALL_DX ),int (MAXIMUM_BALL_DX))
					while dy==0:
						dy=random.randint(int(MINIMUM_BALL_DY ),int (MAXIMUM_BALL_DY))


					i.goto(x,y)
					i.dx=dx
					i.dy=dy
					i.r=r
					i.color(color)
					i.shapesize(r/10)
					my_ball.shapesize(my_ball.r/10)
	return True

def movearound(event):
	my_ball.goto(event.x - SCREEN_WIDTH,SCREEN_HEIGHT - event.y)

turtle.getcanvas().bind("<Motion>", movearound)


turtle.getscreen().listen()

















					


						










mainloop()
