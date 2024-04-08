#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Void, Point, Segment, Polygon


def void_draw(self, tk):
    pass


def point_draw(self, tk):
    tk.draw_point(self.p)


def segment_draw(self, tk):
    tk.draw_line(self.p, self.q)


def polygon_draw(self, tk):
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first())
        self.points.push_last(self.points.pop_first())


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)

tk = TkDrawer()
f = Void()
tk.clean()

p1 = R2Point(1.0, 1.0)
p2 = R2Point(4.0, 1.0)
p3 = R2Point(2.0, 4.0)

try:
    while True:
        f = f.add(R2Point())
        tk.clean()
        tk.draw_line(p1, p3)
        tk.draw_line(p2, p3)
        tk.draw_line(p1, p2)
        f.draw(tk)
        print(f"S = {f.area()}, P = {f.perimeter()}\n")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
