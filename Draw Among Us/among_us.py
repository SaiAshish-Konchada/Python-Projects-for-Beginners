import turtle

#setting the body and glass color
BODY_COLOR = 'red'
GLASS_COLOR = '#9acedc'

#declaring the virtual canvas and turtle
s = turtle.getscreen()
t = turtle.Turtle()

#setting pen size of 20
t.pensize(20)

def body():

    #initialising the color
    t.fillcolor(BODY_COLOR)
    t.begin_fill()

    # drawing the right side
    t.right(90)
    t.forward(50)
    t.right(180)
    t.circle(40, -180)
    t.right(180)
    t.forward(200)

    # drawing the head curve
    t.right(180)
    t.circle(100, -180)

    # drawing the left side
    t.backward(20)
    t.left(15)
    t.circle(500, -20)
    t.backward(20)
    t.circle(40, -180)
    t.left(7)
    t.backward(50)

    # drawing the hip of the body
    t.up()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.down()
    t.right(240)
    t.circle(50, -70)

    #filling the color
    t.end_fill()

def glass():

    #repositioning the turtle
    t.up()
    t.right(230)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.down()

    #initialising the color
    t.fillcolor(GLASS_COLOR)
    t.begin_fill()
    
    #drawing the '(' arc of the glass
    t.right(150)
    t.circle(90, -55)

    #drawing a curve and upper stroke of glass
    t.right(180)
    t.forward(1)
    t.right(180)
    t.circle(10, -65)
    t.right(180)
    t.forward(110)
    t.right(180)

    #drawing the ')' arc of the glass
    t.circle(50, -190)
    t.right(170)
    t.forward(80)

    #drawing the lower curve of glass
    t.right(180)
    t.circle(45, -30)

    #filling the color
    t.end_fill()

def bag():

    #repositioning the turtle
    t.up()
    t.right(60)
    t.forward(100)
    t.right(90)
    t.forward(75)

    #initialising color
    t.fillcolor(BODY_COLOR)
    t.begin_fill()

    #adding bottom stroke of bag
    t.down()
    t.forward(30)
    t.right(255)

    #adding curve of the bag
    t.circle(300, -30)
    t.right(260)

    #adding upper stroke of bag
    t.forward(30)

    #filling the color
    t.end_fill()

body()
glass()
bag()

t.screen.exitonclick()
