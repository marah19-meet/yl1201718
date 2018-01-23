def gameOver():
    edgy_turtle.clear()
    screenMinX = -screen.window_width()/2
    screenMinY = -screen.window_height()/2
    screenMaxX = screen.window_width()/2
    screenMaxY = screen.window_height()/2
    screen.bgcolor("black")
    goto(0, screenMaxY - 350)
    color('grey')
    write("GAME OVER!!", align="center", font=("Arial",50))

    color('black')
    
    turtle.stamp()bbb