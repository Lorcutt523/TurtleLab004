import turtle
import random

"""PUT YOUR FUNCTIONS HERE"""
def draw_square(t,  length):
    """Draws a square with the given side length."""
    for _ in range(4):
        t.forward(length)
        t.left(90)

def draw_circle(t, radius):
    """Draws a circle with the given radius."""
    t.circle(radius)

def draw_polygon(t, sides, length):
    """Draws a regular polygon with a given number of sides and side length."""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

def draw_eye(t, x, y, size):
    """Draws one triangular eye at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()

def draw_mouth(t, x, y, width):
    """Draws a jagged mouth using a series of connected lines."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.right(60)
    for _ in range(5):  # Create a simple zigzag mouth
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)
        t.right(120)
    t.end_fill()
    t.left(60)

def draw_pumpkin(t, x, y, radius):
    """Draws a pumpkin (orange circle) at the given (x, y) location with a green stem."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Drawing the stem
    base = radius // 5
    side = radius // 2
    t.penup()
    t.goto(x - base//2, y+2*.99*radius)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.left(90)  # Point upwards
    t.forward(side)
    t.left(90)
    t.forward(base)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(base)
    t.end_fill()

def draw_star(t, x, y, size):
    """Draws a star at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)  # 144 degrees is the angle to form a star
    t.end_fill()

def draw_jackolantern(t, x, y, r):
    draw_pumpkin(t,x,y,r)
    s = .25*r
    #RIGHT EYE
    draw_eye(t, x - r //2-s//2,y+(2*r) -r//2,s)
    #LEFT EYE
    draw_eye(t, x+r//2-s//2,y+(2*r)-r//2,s)
    draw_mouth(t, x - r // 2, y + r // 2, r)

def draw_sky(t, num_stars):
    """Draws a starry sky with the given number of stars."""
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(100, 300)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)

# Example usage

# Example usage

# Create a turtle object
t = turtle.Turtle()
t.shape("turtle")
t.color("red")

# Hide the turtle and set speed
t.speed(10)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()

# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("blue")
# Set the width and height of the screen
screen.setup(width=1200, height=800)
# Clear the screen
t.clear()

"""PUT YOUR DRAW CALLS TO FUNCTIONS HERE"""
# Example usage
#draw_square(t, 100)
#draw_circle(t, 50)
#draw_polygon(t, 6, 50)  # Hexagon
x = -200
y = -325
r = 100
draw_jackolantern(t,x,y,r)
draw_jackolantern(t, x+300, y, r+4)
draw_jackolantern(t, x-300, y, r+2)

#draw_star(t, -100, 150, 30)  # Star in the sky
#draw_star(t, 100, 180, 20)
draw_sky(t, 50)  # Draw 20 stars

# Close the turtle graphics window when clicked
turtle.exitonclick()