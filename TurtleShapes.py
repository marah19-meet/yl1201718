import turtle
#turtle.speed(10)
#turtle.pensize(5)
#turtle.color("blue")
#for i in range(5):
#	turtle.forward(100)
#	turtle.left(144)
#turtle.mainloop()

turtle.register_shape("pentagon",((0,0),(50,0),(50,-50),(25,-70),(0,-50)))
turtle.shape("pentagon")
turtle.mainloop()

