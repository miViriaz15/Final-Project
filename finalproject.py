'''
miViriaz15 Final Project - turtle graphics in ggame
https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, PolygonAsset, EllipseAsset, CircleAsset
from ggame.line import LineSegment
from math import pi, cos, sin 

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
    def __init__(self):
        super().__init__()
        self.run()
        #Screen.app=App()
        #Screen.app.run()
        
    def step(self):
        for s in self.getSpritesbyClass(Turtle):
            s.step()
            
class Turtle(Sprite):
    #defining colors
    black = Color(0x000000, 1.0)
    white = Color(0xFFFFFF, 1.0)
    thinlinewhite = LineStyle(1, white)
    thinlineblack = LineStyle(1, black)
    def __init__(self):
        width=Screen.width
        height=Screen.height
        screencenter=(width/2,height/2)  #finds a tuple for the center of the screen
        startturtle=PolygonAsset([(5,5),(20,13),(5,21),(10,13),(5,5)],self.thinlineblack, self.black)
        super().__init__(startturtle, screencenter)
        self.rotationgoal=None
        self.forwardgoal=None
        
        self.vr = 0
        self.fxcenter = 1
        self.fycenter = 1/2
        
        self.vx = 0
        self.vy = 0
       
        self.commandlist = []
        self.currentcmd = None
        
        self.distance = 0
        
        self.combinedhead=0
        
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
                #self.forwardgoal = val
                self.vx=-1*cos(self.rotation)
                self.vy=sin(self.rotation)
                if self.forwardgoal==None:
                    self.currentcmd=None
                    
        
        
        elif self.commandlist:
            self.currentcmd = self.commandlist.pop(0)
            cmd,val = self.currentcmd
            
            if cmd=="right":
                self.rotationgoal = self.rotation - val*pi/180
                
            if cmd=="left":
                self.rotationgoal = self.rotation + val*pi/180
                
            if cmd=="forward":
                self.forwardgoal = val + ((self.x-(Screen.width/2))**2+(self.y-(Screen.height/2))**2)**(1/2)  
        
        if not self.rotationgoal is None:    #TURNS
        
            if self.rotationgoal - self.rotation < 0:         #right turn
                if self.rotation + self.vr <= self.rotationgoal:
                    self.vr = 0
                    self.rotation=self.rotationgoal
                    self.rotationgoal=None
                    self.currentcmd=None
                else:
                    self.rotation += self.vr
                
                        
            elif self.rotationgoal - self.rotation > 0:         #left turn
                if self.rotation + self.vr >= self.rotationgoal:
                    self.vr=0
                    self.rotation=self.rotationgoal
                    self.rotationgoal=None
                    self.currentcmd=None
                else:
                    self.rotation += self.vr
                        
            if self.rotation == self.rotationgoal:
                self.vr = 0
                self.rotationgoal=None
                self.currentcmd=None
        
        if not self.forwardgoal is None: #forward
            
            if self.forwardgoal - self.distance > 0:
                
                if self.distance + (self.vx**2+self.vy**2)**1/2 >= self.forwardgoal:
                    self.vx = 0
                    self.vy = 0

                    self.x = (self.forwardgoal - self.distance)*cos(self.rotation) + self.x
                    self.y  = (self.forwardgoal - self.distance)*sin(self.rotation) + self.y
                    
                    self.distance = 0
                    #(self.x**2+self.y**2)**1/2
                    self.forwardgoal=None
                    self.currentcmd=None
                else:
                    self.x -= self.vx
                    self.y -= self.vy
                    line = LineSegment((self.x,self.y), (self.x - self.vx, self.y - self.vy), positioning = "physical")
                    self.distance = ((self.x-(Screen.width/2))**2+(self.y-(Screen.height/2))**2)**(1/2)
                    
            
            if self.distance==self.forwardgoal:
                self.vx = 0
                self.vy = 0
                self.forwardgoal=None
                self.currentcmd=None
                print(self.x, self.y)
                print(((self.x-(Screen.width/2))**2+(self.y-(Screen.height/2))**2)**(1/2))
        

        
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
        self.commandlist.append(("forward",x))
    
    def fd(self,x):
        return self.forward(x)
    
    def backward(self,x):
        self.commandlist.append(("backward",x))
    
    def bk(self,x):
        return self.backward(x)
   
    def back(self,x):
        return self.backward(x)   
   
    
    
    #position, direction, penstate, color
Screen()
alex=Turtle()
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



print(alex.commandlist)
'''myapp.run()


__main__'''