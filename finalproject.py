'''
miViriaz15 Final Project - turtle graphics in ggame
https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, PolygonAsset, EllipseAsset, CircleAsset
from ggame.line import LineSegment
from math import pi, cos, sin, sqrt

#myapp = App()
#defining colors
#black = Color(0x000000, 1.0)
#white = Color(0xFFFFFF, 1.0)


#defining line
#thinlinewhite = LineStyle(1, white)
#thinlineblack = LineStyle(1, black)

#Sprite(PolygonAsset([(5,5),(20,13),(5,21),(10,13),(5,5)],thinlineblack, black))

class Screen(App):
    '''Return the singleton screen object.
    If none exists at the moment, create a new one and return it,
    else return the existing one'''
    app=None
    theturtle = None

    def __init__(self):
        super().__init__()
        self.run()
        #Screen.app=App()
        #Screen.app.run()
        
    def step(self):
        self.theturtle.step()
        #for s in self.getSpritesbyClass(Turtle):
        #    s.step()
            
    @classmethod
    def registerturtle(cls, turtle):
        cls.theturtle = turtle
            
class Turtle:
    #defining colors
    black = Color(0x000000, 1.0)
    red = Color(0xF01414, 1.0)
    white = Color(0xFFFFFF, 1.0)
    blue = Color(0x1464F0, 1.0) 
    green = Color(0x54C175, 1.0)
    yellow = Color(0xFAFF44, 1.0)
    orange = Color(0xFFA500, 1.0)
    cyan = Color(0x00FFFF, 1.0)
    
    thinlinewhite = LineStyle(1, white)
    thinlineblack = LineStyle(1, black)
    thinlinered = LineStyle(1, red)
    thinlineblue = LineStyle(1, blue)
    thinlinegreen = LineStyle(1, green)
    thinlineyellow = LineStyle(1, yellow)
    thinlineorange = LineStyle(1, orange)
    thinlinecyan = LineStyle(1, cyan)
    
    def __init__(self):
        Screen.registerturtle(self)
        self.currentcolor = self.black
        self.currentthinline = self.thinlineblack
        width=Screen.width
        height=Screen.height
        screencenter=(width/2,height/2)  #finds a tuple for the center of the screen
        #self.newturtle(self.currentcolor, self.currentthinline)
        startturtle=PolygonAsset([(5,5),(20,13),(5,21),(10,13),(5,5)],self.currentthinline, self.currentcolor)
        self.turtle = Sprite(startturtle, screencenter)
        self.rotationgoal = None
        self.forwardgoal = None
        self.bkgoal = None
        
        self.vr = 0
        self.turtle.fxcenter = 1
        self.turtle.fycenter = 1/2
        
        self.vx = 0
        self.vy = 0
       
        self.commandlist = []
        self.currentcmd = None
        
        self.distance = 0
        
        self.combinedhead = 0
        
        self.fdx = width/2
        self.fdy = height/2
        
    def newturtle(self, color, line):
        if self.turtle:
            x = self.turtle.x
            y = self.turtle.y
            r = self.turtle.rotation
            self.turtle.destroy()
        else:
            x = self.turtle.x
            y = self.turtle.y
            r = self.turtle.rotation
            startturtle=PolygonAsset([(5,5),(20,13),(5,21),(10,13),(5,5)],self.currentthinline, self.currentcolor)
            self.turtle = Sprite(startturtle, screencenter)
            self.turtle.x = x
        self.turtle.fxcenter = 1
        self.turtle.fycenter = 1/2
        
    def step(self):
        
        if self.currentcmd:
            
            cmd,val = self.currentcmd
            if cmd=="right":
                self.vr = -0.06
                if self.rotationgoal==None:
                    self.currentcmd=None
            
            if cmd=="left": 
                self.vr = 0.06
                if self.rotationgoal==None:
                    self.currentcmd=None   
            
            if cmd=="forward":
                self.vx=-1*cos(self.turtle.rotation)
                self.vy=sin(self.turtle.rotation)
                if self.forwardgoal==None:
                    self.currentcmd=None
                    
            if cmd=="backward":
                self.vx=-cos(self.turtle.rotation)
                self.vy=sin(self.turtle.rotation)
                if self.bkgoal==None:
                    self.currentcmd=None
            
            
        
        elif self.commandlist:
            self.currentcmd = self.commandlist.pop(0)
            cmd,val = self.currentcmd
            
            if cmd=="right":
                self.rotationgoal = self.turtle.rotation - val*pi/180
                
            if cmd=="left":
                self.rotationgoal = self.turtle.rotation + val*pi/180
                
            if cmd=="forward":
                self.forwardgoal =  val
                
            if cmd=="backward":
                self.bkgoal =  val 
                
            if cmd=="color":
                if val == "red":
                    self.currentcolor = self.red
                    self.currentthinline = self.thinlinered
                if val == "black":
                    self.currentcolor = self.black
                    self.currentthinline = self.thinlineblack
                if val == "blue":
                    self.currentcolor = self.blue
                    self.currentthinline = self.thinlineblue  
                if val == "green":
                    self.currentcolor = self.green
                    self.currentthinline = self.thinlinegreen 
                if val == "yellow":
                    self.currentcolor = self.yellow
                    self.currentthinline = self.thinlineyellow
                if val == "orange":
                    self.currentcolor = self.orange
                    self.currentthinline = self.thinlineorange 
                if val == "cyan":
                    self.currentcolor = self.cyan
                    self.currentthinline = self.thinlinecyan 
                self.currentcmd = None
                
        if not self.rotationgoal is None:    #TURNS
        
            if self.rotationgoal - self.turtle.rotation < 0:         #right turn
                if self.turtle.rotation + self.vr <= self.rotationgoal:
                    self.vr = 0
                    self.turtle.rotation=self.rotationgoal
                    self.rotationgoal=None
                    self.currentcmd=None
                else:
                    self.turtle.rotation += self.vr
                
                        
            elif self.rotationgoal - self.turtle.rotation > 0:         #left turn
                if self.turtle.rotation + self.vr >= self.rotationgoal:
                    self.vr = 0
                    self.turtle.rotation = self.rotationgoal
                    self.rotationgoal = None
                    self.currentcmd = None
                else:
                    self.turtle.rotation += self.vr
                        
            if self.turtle.rotation == self.rotationgoal:
                self.vr = 0
                self.turtle.rotation = self.rotationgoal
                self.rotationgoal = None
                self.currentcmd = None
        
        if not self.forwardgoal is None: #forward
            
            if self.forwardgoal - self.distance > 0:
                
                if self.distance + (self.vx**2+self.vy**2)**1/2 >= self.forwardgoal:
                    self.vx = 0
                    self.vy = 0

                    self.turtle.x = (self.forwardgoal - self.distance)*cos(self.turtle.rotation) + self.turtle.x
                    self.turtle.y  = (self.forwardgoal - self.distance)*sin(self.turtle.rotation) + self.turtle.y
                    
                    
                    self.distance = 0
                    
                    self.fdx = self.turtle.x
                    self.fdy = self.turtle.y
                    self.forwardgoal=None
                    self.currentcmd=None
                else:
                    self.turtle.x -= self.vx
                    self.turtle.y -= self.vy
                    line = LineSegment((self.turtle.x,self.turtle.y), (self.turtle.x - self.vx, self.turtle.y - self.vy), style = self.currentthinline, positioning = "physical")
                    self.distance = ((self.turtle.x-self.fdx)**2+(self.turtle.y-self.fdy)**2)**(1/2)
                    
            
            else:
                self.vx = 0
                self.vy = 0
                self.forwardgoal = None
                self.currentcmd = None
                self.fdx = self.turtle.x
                self.fdy = self.turtle.y

                self.distance = 0
               
            
        if not self.bkgoal is None: #backward
            
            if self.bkgoal - self.distance > 0:
                
                if self.distance + (self.vx**2+self.vy**2)**1/2 >= self.bkgoal:
                    self.vx = 0
                    self.vy = 0

                    self.turtle.x = (self.bkgoal - self.distance)*cos(self.turtle.rotation) + self.turtle.x
                    self.turtle.y  = (self.bkgoal - self.distance)*sin(self.turtle.rotation) + self.turtle.y
                    
                    self.distance = 0
                    self.fdx = self.turtle.x
                    self.fdy = self.turtle.y
                    self.bkgoal=None
                    self.currentcmd=None
                else:
                    self.turtle.x += self.vx
                    self.turtle.y += self.vy
                    line = LineSegment((self.turtle.x,self.turtle.y), (self.turtle.x - self.vx, self.turtle.y - self.vy), positioning = "physical")
                    self.distance = ((self.turtle.x-self.fdx)**2+(self.turtle.y-self.fdy)**2)**(1/2)
                    
            
            else:
                self.vx = 0
                self.vy = 0
                self.bkgoal = None
                self.currentcmd = None
                self.fdx = self.turtle.x
                self.fdy = self.turtle.y
                self.distance = 0   

        
    def right(self,x):
        ''' Turn turtle right by angle units.
    
        Aliases: right | rt
    
        Argument:
        angle -- a number (integer or float)
    
        Turn turtle right by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)
    
        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.right(45)
        >>> turtle.heading()
        337.0'''
        
        self.commandlist.append(("right",x))
        
        self.combinedhead -= x
        if self.combinedhead < 0:
            self.combinedhead=-(-self.combinedhead%360)+360
        if self.combinedhead > 0:
            self.combinedhead=self.combinedhead%360
        
    def rt(self,x):
        ''' Turn turtle right by angle units.
    
        Aliases: right | rt
    
        Argument:
        angle -- a number (integer or float)
    
        Turn turtle right by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)
    
        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.right(45)
        >>> turtle.heading()
        337.0'''
        
        return self.right(x)

    def left(self,x):
        '''Turn turtle left by angle units.
    
        Aliases: left | lt
    
        Argument:
        angle -- a number (integer or float)
    
        Turn turtle left by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)
    
        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.left(45)
        >>> turtle.heading()
        67.0'''
        
        self.commandlist.append(("left",x))
        
        self.combinedhead += x
        if self.combinedhead < 0:
            self.combinedhead=-(-self.combinedhead%360)+360
        if self.combinedhead > 0:
            self.combinedhead=self.combinedhead%360
            
    def lt(self,x):
        '''Turn turtle left by angle units.
    
        Aliases: left | lt
    
        Argument:
        angle -- a number (integer or float)
    
        Turn turtle left by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)
    
        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.left(45)
        >>> turtle.heading()
        67.0'''
        
        return self.left(x)
       
    
    def heading(self):
        return self.combinedhead 
    
    def forward(self,x):
        '''Move the turtle forward by the specified distance.
        
        Aliases: forward | fd
        
        Argument:
        distance -- a number (integer or float)
        
        Move the turtle forward by the specified distance, in the direction
        the turtle is headed.
        
        Example:
        >>> position()
        (0.00, 0.00)
        >>> forward(25)
        >>> position()
        (25.00,0.00)
        >>> forward(-75)
        >>> position()
        (-50.00,0.00)'''
    
        self.commandlist.append(("forward",x))
    
    def fd(self,x):
        '''Move the turtle forward by the specified distance.
        
        Aliases: forward | fd
        
        Argument:
        distance -- a number (integer or float)
        
        Move the turtle forward by the specified distance, in the direction
        the turtle is headed.
        
        Example:
        >>> position()
        (0.00, 0.00)
        >>> forward(25)
        >>> position()
        (25.00,0.00)
        >>> forward(-75)
        >>> position()
        (-50.00,0.00)'''
        
        return self.forward(x)
    
    def backward(self,x):
        '''Move the turtle backward by distance.
    
        Aliases: back | backward | bk
    
        Argument:
        distance -- a number
    
        Move the turtle backward by distance ,opposite to the direction the
        turtle is headed. Do not change the turtle's heading.
    
        Example:
        >>> position()
        (0.00, 0.00)
        >>> backward(30)
        >>> position()
        (-30.00, 0.00)'''
        
        self.commandlist.append(("backward",x))
    
    def bk(self,x):
        '''Move the turtle backward by distance.
    
        Aliases: back | backward | bk
    
        Argument:
        distance -- a number
    
        Move the turtle backward by distance ,opposite to the direction the
        turtle is headed. Do not change the turtle's heading.
    
        Example:
        >>> position()
        (0.00, 0.00)
        >>> backward(30)
        >>> position()
        (-30.00, 0.00)'''
        
        return self.backward(x)
   
    def back(self,x):
        '''Move the turtle backward by distance.
    
        Aliases: back | backward | bk
    
        Argument:
        distance -- a number
    
        Move the turtle backward by distance ,opposite to the direction the
        turtle is headed. Do not change the turtle's heading.
    
        Example:
        >>> position()
        (0.00, 0.00)
        >>> backward(30)
        >>> position()
        (-30.00, 0.00)'''
        
        return self.backward(x)
    
    def color(self, x):
        self.commandlist.append(("color",x))
   
    
    
    #position, direction, penstate, color
Screen() # Creates a playground for turtles


'''
spiral=Turtle()
for i in range(500): # this "for" loop will repeat these functions 500 times
    spiral.forward(i)
    spiral.left(91)
'''

star = Turtle()

star.color("green")

for i in range(5):
    star.forward(100)
    star.right(144)



'''
import math #PETALS
radius=100
petals=4

bob=Turtle()
def draw_arc(b,r):  #bob the turtle,corner-to-corner length (radius) of petal (assume 60 degree central angle of sector for simplicity)
    c=2*math.pi*r #Circumference of circle
    ca=c/(360/60)  #Circumference of arc (assume 60 degree central angle of sector as above)
    n=int(ca/3)+1  #number of segments
    l=ca/n  #length of segment
    for i in range(n):
        b.fd(l)
        b.lt(360/(n*6))


def draw_petal(b,r):
    draw_arc(b,r)
    b.lt(180-60)
    draw_arc(b,r)
    b.rt(360/petals-30)  # this will take care of the correct angle b/w petals

for i in range(petals):
    draw_petal(bob,radius)
    bob.lt(360/4)
'''
'''
turtle = Turtle()
distance=20 #spiral

for i in range(17):
    turtle.forward(distance)
    turtle.left(90)
    distance=distance+30


'''
alex = Turtle()
'''
alex.bk(100)
alex.rt(60)
alex.bk(100)
alex.rt(60)
alex.bk(100)
alex.rt(60)
alex.bk(100)
alex.rt(60)
alex.bk(100)
alex.rt(60)
alex.bk(100)

'''
alex.lt(60)
alex.fd(100)
alex.lt(60)
alex.fd(100)
alex.lt(60)
alex.fd(100)
alex.lt(60)
alex.fd(100)
alex.lt(60)
alex.fd(100)
alex.lt(60)
alex.fd(100)


'''myapp.run()


__main__'''