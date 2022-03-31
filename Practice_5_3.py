import turtle

turtle.shape("turtle")
turtle.fillcolor("green")
turtle.speed(2)

def draw(rad, j):
    turtle.circle(rad, 360, 3 + j)
    turtle.up()
    turtle.setpos(0, -rad)
    turtle.down()

for i in range(10):
    draw(30 + 30 * i, i)
