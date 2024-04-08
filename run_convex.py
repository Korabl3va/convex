#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void
from convex import Figure
from deq import Deq

# p1 = R2Point(1.0, 1.0)
# p2 = R2Point(4.0, 1.0)
# p3 = R2Point(2.0, 4.0)

f = Void()
t = Deq()
count, i = 0, 0
Figure._count = 0
try:
    print('Triangle :')
    p1 = R2Point()
    p2 = R2Point()
    p3 = R2Point()
    t = Deq()
    t.push_first(p2)
    if p2.is_light(p1, p3):
        t.push_first(p1)
        t.push_last(p3)
    else:
        t.push_last(p1)
        t.push_first(p3)
    Figure.fixed_triangle = t
    print('Convex :')
    while True:
        f = f.add(R2Point())
        print(f"Кол-во точек = {f.g()}")
        print()
except (EOFError, KeyboardInterrupt):
    print("\nStop")
