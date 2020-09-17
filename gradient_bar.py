import graphics as g

win = g.GraphWin("Gradient Bar", 400, 400)

bar_one_rectangle = Rect1(g.Point(67,0),g.Point(0,400))
color_one = color_rgb(0,0,0)
bar_one_rectangle.setFill(color_one)
bar_one_rectangle.draw(win)

bar_two_rectangle = Rect2(g.Point(134,0),g.Point(67,400))
color_two = color_rgb(0, int(255/6), 0)
bar_two_rectangle.setFill(color_two)
bar_two_rectangle.draw(win)

bar_three_rectangle = Rect3(g.Point(201,0),g.Point(134,400))
color_three = color_rgb(0, int(255/5), 0)
bar_three_rectangle.setFill(color_three)
bar_three_rectangle.draw(win)

bar_four_rectangle = Rect4(g.Point(268,0),g.Point(201,400))
color_four = color_rgb(0, int(255/4), 0)
bar_four_rectangle.setFill(color_four)
bar_four_rectangle.draw(win)

bar_five_rectangle = Rect5(g.Point(335,0),g.Point(268,400))
color_five = color_rgb(0, int(255/3), 0)
bar_five_rectangle.setFill(color_five)
bar_five_rectangle.draw(win)

bar_six_rectangle = Rect6(g.Point(400,0),g.Point(335,400))
color_six = color_rgb(0, int(255/2), 0)
bar_six_rectangle.setFill(color_six)
bar_six_rectangle.draw(win)
