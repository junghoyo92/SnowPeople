#########################
##CSE231 section 2     ##
#########################

import math
import turtle
import time

class Line(object):
    """Line class"""
    def __init__(self, beg = (0.0, 0.0), end = (50.0, 0.0),
                 pencolor = "black", pensize = 1):
        """
        create a line starting from the coordinates given by beg to
        the coordinates given by end
        """
        self.pencolor = pencolor
        self.pensize  = pensize
        self.beg = beg
        self.end = end
        self.tag = "Line"

    def __str__(self):
        return "%s(%s,%s)" % (self.tag,self.beg,self.end)

    def draw(self,pen):
        """draw the line using the provided pen"""
        pen.pencolor(self.pencolor)
        pen.pensize(self.pensize)
        if pen.pos() != self.beg:
            pen.up()
            pen.goto(self.beg)
        pen.down()
        pen.goto(self.end)

class Polygon(object):
    """Polygon class"""
    def __init__(self, vertices = [],
                 fillcolor = "", pencolor = "black", pensize = 1):
        """
        create a polygon from a list of its vertices
        """
        self.vertices = vertices
        self.pencolor, self.fillcolor, self.pensize = pencolor, fillcolor, pensize
        self.tag = "Poly"

    def __str__(self):
        vertexStr = ",".join([str(v) for v in self.vertices])
        return "%s(%s)" % (self.tag,vertexStr)

    """Draws a polygon, used to generate the triangle and rectangle through inheritance"""

    def draw(self, pen):
        lines = []
        vertices = self.vertices
        if vertices:
            for i in range(len(vertices)-1):
                lines.append(Line(vertices[i],vertices[i+1], self.pencolor))
            lines.append(Line(vertices[-1],vertices[0]))
        pen.color(self.pencolor, self.fillcolor)
        if self.fillcolor: pen.begin_fill()
        for l in lines:
            l.draw(pen)
        pen.end_fill()

class Triangle(object):
    """Triangle Class"""
    def __init__(self, point_a = (0.0,0.0), point_b = (5.0,0.0), point_c = (0.0,5.0), fillcolor = "", pencolor = "black", pensize = 1):
        """
        Create a triangle out of thin air
        """
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.pencolor, self.fillcolor, self.pensize = pencolor, fillcolor, pensize
        self.tag = "Triangle"

    def __str__(self):
        point_a = str(self.point_a)
        point_b = str(self.point_b)
        point_c = str(self.point_c)
        return "%s(%s,%s,%s)" % (self.tag,point_a,point_b,point_c)

    """Draws a Triangle"""
    
    def draw(self,pen):
        vertices = []
        vertices.append(self.point_a)
        vertices.append(self.point_b)
        vertices.append(self.point_c)
        fillcolor = self.fillcolor
        pencolor = self.pencolor
        pensize = self.pensize
        Polygon(vertices,fillcolor,pencolor, pensize).draw(pen)
        

class Rectangle(object):
    """Rectangle Class"""
    def __init__(self, low_left = (0.0,0.0), up_right = (5.0,5.0), fillcolor = "", pencolor = "black", pensize = 1):
        """
        Create a rectangle
        """
        self.low_left = low_left
        self.up_right = up_right
        self.low_right = (up_right[0],low_left[1])
        self.up_left = (low_left[0],up_right[1])
        self.pencolor, self.fillcolor, self.pensize = pencolor, fillcolor, pensize
        self.tag = "Rectangle"

    def __str__(self):
        low_left = str(self.low_left)
        up_right = str(self.up_right)
        return "%s(%s,%s)" % (self.tag,low_left,up_right)

    """Draws a retangle"""
    
    def draw(self,pen):
        vertices = []
        vertices.append(self.low_left)
        vertices.append(self.low_right)
        vertices.append(self.up_right)
        vertices.append(self.up_left)
        fillcolor = self.fillcolor
        pencolor = self.pencolor
        pensize = self.pensize
        Polygon(vertices,fillcolor,pencolor,pensize).draw(pen)

class Circle(object):
    """Circle Class"""
    def __init__(self, center = (0.0,0.0), radius = 5.0, fillcolor = "", pencolor = "black", pensize = 1):
        self.center = center
        self.radius = radius
        self.pencolor, self.fillcolor, self.pensize = pencolor, fillcolor, pensize
        self.tag = "Circle"

    def __str__(self):
        centerStr = str(self.center)
        return "%s(%s,%s)" % (self.tag,centerStr,self.radius)

    """Draws a circle"""
    
    def draw(self,pen):
        pen.color(self.pencolor, self.fillcolor)
        pensize = self.pensize
        pen.pensize(pensize)
        center = self.center
        pen.up()
        pen.goto(center[0],center[1])
        pen.down()
        if self.fillcolor: pen.begin_fill()
        pen.circle(self.radius)
        pen.end_fill()

class Snowperson(object):
    """Snow Person Class"""
    def __init__(self, position = (0.0,0.0), size = 30.0, fillcolor = "", pencolor = "black", pensize = 1):
        self.position = position
        self.size = size
        self.pencolor = pencolor
        self.fillcolor = fillcolor
        self.pensize = pensize
        self.tag = "Snowperson"

    def __str__(self):
        return "%s(%s,%s)" % (self.tag, str(self.beg), str(self.size))
    
    """Creates the basic body of a snowman. (3 snowballs)"""
    
    def draw(self, pen):
        position = self.position
        radius = self.size
        pencolor = self.pencolor
        fillcolor = self.fillcolor
        pensize = self.pensize
        Circle(position,radius,fillcolor, pencolor, pensize).draw(pen)
        position2 = (position[0],position[1]+(1.98*radius))
        radius2 = radius/1.25
        Circle(position2, radius2, fillcolor, pencolor, pensize).draw(pen)
        position3 = (position2[0],position2[1]+(1.98*radius2))
        radius3 = radius/1.875
        Circle(position3, radius3, fillcolor, pencolor, pensize).draw(pen)

class Snowman(object):
    """Snow Man Class"""
    def __init__(self, position = (0.0,0.0), size = 30.0, fillcolor = "", pencolor = "black", pensize = 1):
        self.position = position
        self.size = size
        self.fillcolor = fillcolor
        self.pencolor = pencolor
        self.pensize = pensize
        self.tag = "Snowman"

    def __str__(self):
        return "%s" % (self.tag)
    
    """ Takes previous classes and creates a snowman with a hat, eyes, nose, mouth, arms, and buttons"""
    def draw(self, pen):
        position = self.position
        size = self.size
        fillcolor = self.fillcolor
        pencolor = self.pencolor
        pensize = self.pensize
        Snowperson(position, size, fillcolor, pencolor,pensize).draw(pen)
        linebeg = (position[0]+(-size/1.875), position[1]+(1.9*(size + size/1.25 + size/1.875)))
        lineend = (position[0]+(size/1.875), position[1]+(1.9*(size + size/1.25 + size/1.875)))
        Line(linebeg, lineend, pencolor = "purple", pensize = 5).draw(pen)
        hatbl = (position[0]+(-size/2.25), position[1]+(1.9*(size + size/1.25 + size/1.875)))
        hatur = (position[0]+(size/2.25), position[1]+(2.15*(size + size/1.25 + size/1.875)))
        Rectangle(hatbl, hatur, fillcolor = "purple", pencolor = "blue").draw(pen)
        lefteye = (position[0]+(-size/4.25), position[1]+(1.75*(size + size/1.25 + size/1.875)))
        eyerad = size/15
        Circle(lefteye, eyerad, fillcolor = "black", pencolor = "black").draw(pen)
        righteye = (position[0]+(size/4.25), position[1]+(1.75*(size + size/1.25 + size/1.875)))
        eyerad = size/15
        Circle(righteye, eyerad, fillcolor = "black", pencolor = "black").draw(pen)
        nose = (position[0], position[1]+(1.7*(size + size/1.25 + size/1.875)))
        noserad = size/15
        Circle(nose, noserad, fillcolor = "orange", pencolor = "orange").draw(pen)
        mouthbeg = (position[0]+(-size/4.5), position[1]+(1.62*(size + size/1.25 + size/1.875)))
        mouthend = (position[0]+(size/4.5), position[1]+(1.62*(size + size/1.25 + size/1.875)))
        mouthmiddle = (position[0], position[1]+(1.6*(size + size/1.25 + size/1.875)))
        Triangle(mouthbeg, mouthend, mouthmiddle, fillcolor = "red", pencolor = "red").draw(pen)
        button = (position[0], position[1]+(1.455*(size + size/1.25 + size/1.875)))
        buttonrad = size/12
        Circle(button, buttonrad, fillcolor = "purple", pencolor = "blue").draw(pen)
        bowtie1 = (position[0]+(-size/3), position[1]+(1.45*(size + size/1.25 + size/1.875)))
        bowtie2 = (position[0], position[1]+(1.5*(size + size/1.25 + size/1.875)))
        bowtie3 = (position[0]+(-size/3), position[1]+(1.55*(size + size/1.25 + size/1.875)))
        Triangle(bowtie1, bowtie2, bowtie3, fillcolor = "purple", pencolor = "blue").draw(pen)
        bowtie4 = (position[0]+(size/3), position[1]+(1.45*(size + size/1.25 + size/1.875)))
        bowtie5 = (position[0], position[1]+(1.5*(size + size/1.25 + size/1.875)))
        bowtie6 = (position[0]+(size/3), position[1]+(1.55*(size + size/1.25 + size/1.875)))
        Triangle(bowtie4, bowtie5, bowtie6, fillcolor = "purple", pencolor = "blue").draw(pen)
        button = (position[0], position[1]+(1.3*(size + size/1.25 + size/1.875)))
        buttonrad = size/12
        Circle(button, buttonrad, fillcolor = "purple", pencolor = "blue").draw(pen)
        button = (position[0], position[1]+(1.15*(size + size/1.25 + size/1.875)))
        buttonrad = size/12
        Circle(button, buttonrad, fillcolor = "purple", pencolor = "blue").draw(pen)
        button = (position[0], position[1]+(size + size/1.25 + size/1.875))
        buttonrad = size/12
        Circle(button, buttonrad, fillcolor = "purple", pencolor = "blue").draw(pen)
        lefthandbeg = (position[0]+(-size/1.5), position[1]+(1.6*(size + size/1.25)))
        lefthandend = (position[0]+(-size), position[1]+(.8*size + size/1.25))
        Line(lefthandbeg, lefthandend, pencolor = "brown", pensize = 10).draw(pen)
        righthandbeg = (position[0]+(size/1.5), position[1]+(1.6*(size + size/1.25)))
        righthandend = (position[0]+(size), position[1]+(.8*size + size/1.25))
        Line(righthandbeg, righthandend, pencolor = "brown", pensize = 10).draw(pen)

class Snowwoman(object):
    """Snow Man Class"""
    def __init__(self, position = (0.0,0.0), size = 30.0, fillcolor = "", pencolor = "black", pensize = 1):
        self.position = position
        self.size = size
        self.fillcolor = fillcolor
        self.pencolor = pencolor
        self.pensize = pensize
        self.tag = "SnowWoman"

    def __str__(self):
        return "%s" % (self.tag)
    
    """ Takes previous classes and creates a snowman with a hat, eyes, nose, mouth, arms, hair, and buttons"""
    def draw(self, pen):
        position = self.position
        size = self.size
        fillcolor = self.fillcolor
        pencolor = self.pencolor
        pensize = self.pensize
        Snowperson(position, size, fillcolor, pencolor, pensize).draw(pen)
        hairbeg = (position[0]+(-size/2), position[1]+(1.9*(size + size/1.25 + size/1.875)))
        hairend = (position[0]+(-size/1.9), position[1]+(1.5*(size + size/1.25 + size/1.875)))
        Line(hairbeg, hairend, pencolor = "pink", pensize = 3).draw(pen)
        hairbeg = (position[0]+(-size/2.2), position[1]+(1.9*(size + size/1.25 + size/1.875)))
        hairend = (position[0]+(-size/2.1), position[1]+(1.5*(size + size/1.25 + size/1.875)))
        Line(hairbeg, hairend, pencolor = "pink", pensize = 3).draw(pen)
        hairbeg = (position[0]+(-size/2.5), position[1]+(1.9*(size + size/1.25 + size/1.875)))
        hairend = (position[0]+(-size/2.1), position[1]+(1.5*(size + size/1.25 + size/1.875)))
        Line(hairbeg, hairend, pencolor = "pink", pensize = 3).draw(pen)
        hairbeg = (position[0]+(-size/2.4), position[1]+(1.9*(size + size/1.25 + size/1.875)))
        hairend = (position[0]+(-size/2.1), position[1]+(1.5*(size + size/1.25 + size/1.875)))
        Line(hairbeg, hairend, pencolor = "pink", pensize = 3).draw(pen)
        hairbeg = (position[0]+(-size/3.5), position[1]+(1.9*(size + size/1.25 + size/1.875)))
        hairend = (position[0]+(-size/2.2), position[1]+(1.5*(size + size/1.25 + size/1.875)))
        Line(hairbeg, hairend, pencolor = "pink", pensize = 3).draw(pen)
        hairbeg = (position[0]+(-size/3.3), position[1]+(1.9*(size + size/1.25 + size/1.875)))
        hairend = (position[0]+(-size/2.2), position[1]+(1.5*(size + size/1.25 + size/1.875)))
        Line(hairbeg, hairend, pencolor = "pink", pensize = 3).draw(pen)
        hairbeg = (position[0]+(-size/3.1), position[1]+(1.9*(size + size/1.25 + size/1.875)))
        hairend = (position[0]+(-size/2.2), position[1]+(1.5*(size + size/1.25 + size/1.875)))
        Line(hairbeg, hairend, pencolor = "pink", pensize = 3).draw(pen)
        hairbeg = (position[0]+(-size/2.9), position[1]+(1.9*(size + size/1.25 + size/1.875)))
        hairend = (position[0]+(-size/2.2), position[1]+(1.5*(size + size/1.25 + size/1.875)))
        Line(hairbeg, hairend, pencolor = "pink", pensize = 3).draw(pen)
        hairbeg = (position[0]+(size/2), position[1]+(1.9*(size + size/1.25 + size/1.875)))
        hairend = (position[0]+(size/1.9), position[1]+(1.75*(size + size/1.25 + size/1.875)))
        Line(hairbeg, hairend, pencolor = "pink", pensize = 3).draw(pen)
        hairbeg = (position[0]+(size/2.2), position[1]+(1.9*(size + size/1.25 + size/1.875)))
        hairend = (position[0]+(size/2.1), position[1]+(1.75*(size + size/1.25 + size/1.875)))
        Line(hairbeg, hairend, pencolor = "pink", pensize = 3).draw(pen)
        hairbeg = (position[0]+(size/2.5), position[1]+(1.9*(size + size/1.25 + size/1.875)))
        hairend = (position[0]+(size/2.1), position[1]+(1.75*(size + size/1.25 + size/1.875)))
        Line(hairbeg, hairend, pencolor = "pink", pensize = 3).draw(pen)
        hairbeg = (position[0]+(size/2.4), position[1]+(1.9*(size + size/1.25 + size/1.875)))
        hairend = (position[0]+(size/2.1), position[1]+(1.75*(size + size/1.25 + size/1.875)))
        Line(hairbeg, hairend, pencolor = "pink", pensize = 3).draw(pen)
        hairbeg = (position[0]+(size/3.5), position[1]+(1.9*(size + size/1.25 + size/1.875)))
        hairend = (position[0]+(size/2.2), position[1]+(1.75*(size + size/1.25 + size/1.875)))
        Line(hairbeg, hairend, pencolor = "pink", pensize = 3).draw(pen)
        hairbeg = (position[0]+(size/3.3), position[1]+(1.9*(size + size/1.25 + size/1.875)))
        hairend = (position[0]+(size/2.2), position[1]+(1.75*(size + size/1.25 + size/1.875)))
        Line(hairbeg, hairend, pencolor = "pink", pensize = 3).draw(pen)
        hairbeg = (position[0]+(size/3.1), position[1]+(1.9*(size + size/1.25 + size/1.875)))
        hairend = (position[0]+(size/2.2), position[1]+(1.75*(size + size/1.25 + size/1.875)))
        Line(hairbeg, hairend, pencolor = "pink", pensize = 3).draw(pen)
        hairbeg = (position[0]+(size/2.9), position[1]+(1.9*(size + size/1.25 + size/1.875)))
        hairend = (position[0]+(size/2.2), position[1]+(1.75*(size + size/1.25 + size/1.875)))
        Line(hairbeg, hairend, pencolor = "pink", pensize = 3).draw(pen)
        hat1 = (position[0]+(-size/1.875), position[1]+(1.9*(size + size/1.25 + size/1.875)))
        hat2 = (position[0]+(size/1.875), position[1]+(1.9*(size + size/1.25 + size/1.875)))
        hat3 = (position[0], position[1]+(2.5*(size + size/1.25 + size/1.875)))
        Triangle(hat1, hat2, hat3, fillcolor = "blue", pencolor = "purple").draw(pen)
        lefteye = (position[0]+(-size/4.35), position[1]+(1.75*(size + size/1.25 + size/1.875)))
        eyerad = size/15
        Circle(lefteye, eyerad, fillcolor = "black", pencolor = "black").draw(pen)
        righteye = (position[0]+(size/4.35), position[1]+(1.75*(size + size/1.25 + size/1.875)))
        eyerad = size/15
        Circle(righteye, eyerad, fillcolor = "black", pencolor = "black").draw(pen)
        nose = (position[0], position[1]+(1.7*(size + size/1.25 + size/1.875)))
        noserad = size/15
        Circle(nose, noserad, fillcolor = "orange", pencolor = "orange").draw(pen)
        mouthbeg = (position[0]+(-size/4.5), position[1]+(1.62*(size + size/1.25 + size/1.875)))
        mouthend = (position[0]+(size/4.5), position[1]+(1.62*(size + size/1.25 + size/1.875)))
        mouthmiddle = (position[0], position[1]+(1.6*(size + size/1.25 + size/1.875)))
        Triangle(mouthbeg, mouthend, mouthmiddle, fillcolor = "red", pencolor = "red").draw(pen)
        button = (position[0], position[1]+(1.3*(size + size/1.25 + size/1.875)))
        buttonrad = size/12
        Circle(button, buttonrad, fillcolor = "blue", pencolor = "pink").draw(pen)
        button = (position[0], position[1]+(1.15*(size + size/1.25 + size/1.875)))
        buttonrad = size/12
        Circle(button, buttonrad, fillcolor = "blue", pencolor = "pink").draw(pen)
        button = (position[0], position[1]+(size + size/1.25 + size/1.875))
        buttonrad = size/12
        Circle(button, buttonrad, fillcolor = "blue", pencolor = "pink").draw(pen)
        lefthandbeg = (position[0]+(-size/1.5), position[1]+(1.6*(size + size/1.25)))
        lefthandend = (position[0]+(-size), position[1]+(.8*size + size/1.25))
        Line(lefthandbeg, lefthandend, pencolor = "brown", pensize = 6).draw(pen)
        righthandbeg = (position[0]+(size/1.5), position[1]+(1.6*(size + size/1.25)))
        righthandend = (position[0]+(size), position[1]+(.8*size + size/1.25))
        Line(righthandbeg, righthandend, pencolor = "brown", pensize = 6).draw(pen)       
        
def Main():
    pen = turtle.Turtle()
    sm = Snowman(position = (-100,-100), size = 75, fillcolor = "white", pencolor = "black", pensize = 1)
    print(sm)
    sm.draw(pen)
    
    sm = Snowwoman(position = (100,-100), size = 40, fillcolor = "white", pencolor = "black", pensize = 1)
    print(sm)
    sm.draw(pen)
    
    pen.hideturtle()
    time.sleep(15)
    turtle.bye()

Main()
