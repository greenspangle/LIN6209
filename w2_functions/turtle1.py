# import the turtle library
# note the different for of the import statement 
from turtle import *

def sq(pencolor, fillcolor):
    color(pencolor, fillcolor)
    begin_fill()
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(200)
    end_fill()


if __name__ == '__main__':
    print("Now call the function sq('blue', 'green')  # choose any standard color")
