import turtle
import time

class Shape(object):
    """General shape class"""
    def __init__(self, pencolor = "black", pensize = 1):
        """
        create a shape
            pencolor - color of the pen to use for outlining
            pensize - size (width) of the pen to use
        """
        self.pencolor = pencolor
        self.pensize = pensize

class Line(Shape):
    """Line class"""
    def __init__(self, beg = (0.0, 0.0), end = (50.0, 0.0),
                 pencolor = "black", pensize = 1):
        """
        create a line
            beg - coordinates of the beginning point
            end - coordinates of the ending point
            pencolor - color of the line
            pensize - size (width) of the line
        """
        Shape.__init__(self,pencolor,pensize)
        self.beg = beg
        self.end = end

    def __str__(self):
        return "Line(beg:{},end:{})".format(self.beg,self.end)

    def draw(self, pen):
        """draw the line using the provided pen"""
        pen.pensize(self.pensize)
        pen.pencolor(self.pencolor)
        pen.up()
        pen.goto(self.beg)
        pen.down()
        pen.goto(self.end)

class Box(object):
    """3-D box class"""
    def __init__(self, pos = (0.0,0.0), size = 50):
        """create a 3-D box given:
             pos - reference position (lower left corner of the box)
             size - length of a side of the box
        """
        self.pos = pos
        x,y = pos
        self.size = size
        offset = size/3.0     # off set to use for back face   
        # an instance contains 9 lines, comments indicate: face, edge
        self.side_lines = [Line((x,y),(x,y+size)), # front, left 
                           Line((x,y),(x+size,y)), # front, bottom
                           Line((x+size,y),(x+size,y+size)),  # front, right
                           Line((x,y+size),(x+size,y+size)),  # front, top
                           Line((x,y+size),(x+offset,y+size+offset)), #top, left
                           Line((x+offset,y+size+offset),(x+size+offset,y+size+offset)), #top, back
                           Line((x+size,y+size),(x+size+offset,y+size+offset)), #top, right
                           Line((x+size,y),(x+size+offset,y+offset)),  # right, bottom
                           Line((x+size+offset,y+offset),(x+size+offset,y+size+offset)) # right, back
                           ]

    def __str__(self):
        return "Box(pos:{},size:{})".format(self.pos,self.size)

    def draw(self,pen):
        for l in self.side_lines:
            l.draw(pen)

def main():
    pen = turtle.Turtle()

    
    box1 = Box()
    print(box1)
    box1.draw(pen)

    box2 = Box((80.0,0.0), 60)
    print(box2)
    box2.draw(pen)

    line = Line((-100,-100),(-100,100),"purple", 3)
    print(line)
    line.draw(pen)
    
    pen.hideturtle()
    time.sleep(5)
    turtle.bye()
    
    

main()
    
