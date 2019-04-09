'''
miViriaz15 Final Project - turtle graphics in ggame
https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, PolygonAsset, EllipseAsset, CircleAsset

#defining colors
black = Color(0x000000, 1.0)
white = Color(0xFFFFFF, 1.0)


#defining line
thinlinewhite = LineStyle(1, white)
thinlineblack = LineStyle(1, black)




class Turtle(Sprite):
    #screencenter
    startturtle=PolygonAsset([(5,5),(25,10),(5,15),(10,10),(5,5)],thinlineblack, white)
    def __init__(self):
        super().__init__(screencenter, startturtle)
    
    #position, direction, penstate, color