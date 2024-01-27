import turtle

turtle.speed(15)
turtle.bgcolor('black')
r, g, b = 25, 0, 0

for i in range(255*2):
    turtle.colormode(255)

    if i <(255*1)//3:
        g+=3
    elif i<(255*2)//3:
        r-=3
    elif i<(255*1)//3:
        b+=3
    elif i<(255*4)//3:
        g-=3
    elif i<(255*5)//3:
        r+=3
    turtle.forward(50+i)
    turtle.right(91)
    turtle.pencolor(r,g,b)

turtle.done()