from turtle import *
import turtle
import time
import random
from ball import Ball
tracer(0)
hideturtle()
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

