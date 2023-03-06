import simple_draw as sd

def drawing_pigchel(center, rad):
    sd.circle(center_position = center,radius=rad, color=(255,0,255), width=0)
    sd.circle(center_position = sd.Point(center.x - 43, center.y + 30),radius=15, color=sd.COLOR_WHITE, width=0)
    sd.circle(center_position = sd.Point(center.x - 43, center.y + 30),radius=5, color=sd.COLOR_BLACK, width=0)
    sd.circle(center_position = sd.Point(center.x + 43, center.y + 30),radius=15, color=sd.COLOR_WHITE, width=0)
    sd.circle(center_position = sd.Point(center.x + 43, center.y + 30),radius=5, color=sd.COLOR_BLACK, width=0)
    point_list1 = [sd.Point(center.x - 63, center.y - 10), sd.Point(center.x - 20, center.y - 55), sd.Point(center.x + 20, center.y - 55), sd.Point(center.x + 63, center.y - 10 )]
    sd.lines(point_list1, closed=False, width=1, color=sd.COLOR_BLACK)
    sd.ellipse(sd.Point(center.x - 43, center.y - 30), sd.Point(center.x + 43, center.y + 14), color=sd.COLOR_BLACK, width=1)
    sd.ellipse(sd.Point(center.x - 35, center.y - 15), sd.Point(center.x - 15, center.y + 5), color=sd.COLOR_BLACK, width=0)
    sd.ellipse(sd.Point(center.x + 35, center.y - 15), sd.Point(center.x + 15, center.y + 5), color=sd.COLOR_BLACK, width=0)

    point_list = [sd.Point(center.x + 43, center.y + rad-10), sd.Point(center.x + 75, center.y + rad-40), sd.Point(center.x + 80, center.y + 120)]
    sd.polygon(point_list, width = 0, color=(255,0,255))
    point_list2 = [sd.Point(center.x + 50, center.y + rad-10), sd.Point(center.x + 70, center.y + rad-32), sd.Point(center.x + 76, center.y + 110)]
    sd.polygon(point_list2, width = 1, color=sd.COLOR_BLACK)

    point_list3 = [sd.Point(center.x - 43, center.y + rad-10), sd.Point(center.x - 75, center.y + rad-40), sd.Point(center.x - 80, center.y + 120)]
    sd.polygon(point_list3, width = 0, color=(255,0,255))
    point_list4 = [sd.Point(center.x - 50, center.y + rad-10), sd.Point(center.x - 70, center.y + rad-32), sd.Point(center.x - 76, center.y + 110)]
    sd.polygon(point_list4, width = 1, color=sd.COLOR_BLACK)