'''
miViriaz15 Final Project - turtle graphics in ggame
https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, PolygonAsset, EllipseAsset, CircleAsset
from math import pi

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
        
        self.vr = 0
        self.fxcenter = 1/3
        self.fycenter = 1/2
       
        self.commandlist = []
        self.currentcmd = None
        
        self.combinedhead=0
        
    def step(self):
        
        if self.currentcmd:
            cmd,val = self.currentcmd
            if cmd=="right":
                self.vr = -0.05
                if self.rotationgoal==None:
                    self.currentcmd=None
            if cmd=="left":
                self.vr = 0.05
                if self.rotationgoal==None:
                    self.currentcmd=None   
        
        elif self.commandlist:
            self.currentcmd = self.commandlist.pop(0)
            cmd,val = self.currentcmd
            
            if cmd=="right":
                self.rotationgoal = self.rotation - val*pi/180
                
            if cmd=="left":
                self.rotationgoal = self.rotation + val*pi/180
        
        if not self.rotationgoal is None:
        
            if self.rotationgoal-self.rotation < 0:         #right turn
                self.rotation += self.vr
                if self.rotation <= self.rotationgoal:
                    self.vr=0
                    self.rotation=self.rotationgoal
                    self.rotationgoal=None
                        
            elif self.rotationgoal-self.rotation > 0:         #left turn
                self.rotation += self.vr
                if self.rotation >= self.rotationgoal:
                    self.vr=0
                    self.rotation=self.rotationgoal
                    self.rotationgoal=None
                        
            if self.rotation == self.rotationgoal:
                self.vr=0
                self.rotationgoal=None
            
        
        

        
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
alex.lt(100)
alex.lt(100)
alex.rt(10)
alex.rt(100)
alex.fd(2)
print(alex.commandlist)
'''myapp.run()


__main__'''