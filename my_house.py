#from graphics import *

import graphics as g


win = g.GraphWin("My House", 700, 500)


DISTANCE_FROM_EDGE_TO_LEFT_WALL = 100
DISTANCE_FROM_TOP_TO_TOP_OF_HOUSE = 300

WIDTH_OF_HOUSE = 200
HEIGHT_OF_HOUSE = 100

SUN_RADIUS = 60


upper_left_point = g.Point(DISTANCE_FROM_EDGE_TO_LEFT_WALL, DISTANCE_FROM_TOP_TO_TOP_OF_HOUSE)

lower_right_point = upper_left_point.clone()
lower_right_point.move(WIDTH_OF_HOUSE, HEIGHT_OF_HOUSE)


roof_peak_point = upper_left_point.clone()
roof_peak_point.move(WIDTH_OF_HOUSE/2, -50)

left_side_roof_line = g.Line(upper_left_point, roof_peak_point)

upper_right_point = lower_right_point.clone()
upper_right_point.move(0,-HEIGHT_OF_HOUSE) 

right_side_roof_line = g.Line(roof_peak_point,upper_right_point)

center_of_sun = roof_peak_point.clone()
center_of_sun.move(-50, -75)

sun = g.Circle(center_of_sun, SUN_RADIUS)
sun.setFill("orange")


sun.draw(win)
right_side_roof_line.draw(win)
left_side_roof_line.draw(win)

house = g.Rectangle(upper_left_point, lower_right_point)
house.setFill("blue")
house.draw(win)


label = g.Text(center_of_sun, "eSmith")
label.draw(win)



win.getMouse()
house.setFill("yellow")
