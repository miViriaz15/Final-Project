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

class Screen:
    app=None
    def __init__(self):
        Screen.app=App()
        Screen.app.run()

class Turtle(Sprite):
    #defining colors
    black = Color(0x000000, 1.0)
    white = Color(0xFFFFFF, 1.0)
    thinlinewhite = LineStyle(1, white)
    thinlineblack = LineStyle(1, black)
    def __init__(self):
        width=Screen.app.width
        height=Screen.app.height
        screencenter=(width/2,height/2)
        startturtle=PolygonAsset([(5,5),(20,13),(5,21),(10,13),(5,5)],self.thinlineblack, self.black)
        super().__init__(startturtle, screencenter)
    def right(x):
        startturtle.rotation(x*pi/180)
        
    
    #position, direction, penstate, color
Screen()
alex=Turtle()
alex.right(90)

'''myapp.run()


__main__'''