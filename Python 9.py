import random
import turtle as t

def get_line_length() :
    choice = input('Enter line length (Long, Medium, Short) : ')
    if choice == 'Long' :
        line_length = 250
    elif choice == 'Medium' :
        line_length = 200
    else :
        line_length = 100
    return line_length

def get_line_width() :
    choice = input('Enter line width (Superthick, Thick, Thin) : ')
    if choice == 'Superthick' :
        line_width = 45
    elif choice == 'Thick' :
        line_width = 25
    else :
        line_width = 10
    return line_width

def inside_window() :
    left_limit = (-t.window_width() / 2) + 100
    right_limit = (t.window_width() / 2) - 100
    top_limit = (t.window_height() / 2) - 100
    bottom_limit = (-t.window_height() / 2) + 100
    (x, y) = t.pos()
    inside = left_limit < x <right_limit and bottom_limit < y < top_limit
    return inside

def move_turtle(line_length) :
    pen_colors = ['red', 'orange', 'yellow', 'green', \
                  'blue', 'purple']
    t.pencolor(random.choice(pen_colors))
    t.fillcolor(random.choice(pen_colors))
    t.shapesize(3, 3, 1)
    t.stamp()
    if inside_window() :
        angle = random.randint(0, 180)
        t.right(angle)
        t.forward(line_length)
    else :
        t.backward(line_length)

line_length = get_line_length()
line_width = get_line_width()

t.shape('turtle')
t.fillcolor('green')
t.bgcolor('black')
t.speed('fastest')
t.pensize(line_width)

while True:
       move_turtle  (line_length)