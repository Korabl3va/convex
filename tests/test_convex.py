from pytest import approx
from math import sqrt

from r2point import R2Point
from convex import Figure, Void, Point, Segment, Polygon
from deq import Deq


class TestVoid:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        Figure._count = 0
        a = R2Point(0.0, 0.0)
        b = R2Point(1.0, 0.0)
        c = R2Point(0.0, 1.0)
        m = Deq()
        m.push_first(b)
        m.push_first(a)
        m.push_last(c)

        Figure.fixed_triangle = m
        self.f = Void()

    # Нульугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Void (нульугольник)
    def test_void(self):
        assert isinstance(self.f, Void)

    # Периметр нульугольника нулевой
    def test_perimeter(self):
        assert self.f.perimeter() == 0.0

    # Площадь нульугольника нулевая
    def test_area(self):
        assert self.f.area() == 0.0

    # При добавлении точки нульугольник превращается в одноугольник
    def test_add(self):
        assert isinstance(self.f.add(R2Point(0.0, 0.0)), Point)

    # Функция `g` вычисляется корректно
    def test_count_points(self):
        assert self.f.g() == 0


class TestPoint:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        Figure._count = 0
        m = Deq()
        a = R2Point(0.0, 0.0)
        b = R2Point(1.0, 0.0)
        c = R2Point(0.0, 1.0)
        m.push_first(b)
        m.push_first(a)
        m.push_last(c)

        Figure.fixed_triangle = m
        self.f = Point(R2Point(0.0, 0.0))

    # Одноугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Point (одноугольник)
    def test_point(self):
        assert isinstance(self.f, Point)

    # Периметр одноугольника нулевой
    def test_perimeter(self):
        assert self.f.perimeter() == 0.0

    # Площадь одноугольника нулевая
    def test_area(self):
        assert self.f.area() == 0.0

    # При добавлении точки одноугольник может не измениться
    def test_add1(self):
        assert self.f.add(R2Point(0.0, 0.0)) is self.f

    # При добавлении точки одноугольник может превратиться в двуугольник
    def test_add2(self):
        assert isinstance(self.f.add(R2Point(1.0, 0.0)), Segment)

    # Функция `g` вычисляется корректно
    def test_count_points_1(self):
        assert self.f.g() == approx(1)

    def test_count_points_2(self):
        self.f = Point(R2Point(-5.0, 1))
        assert self.f.g() == approx(0)


class TestSegment:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        Figure._count = 0
        Figure._count = 0
        a = R2Point(0.0, 0.0)
        b = R2Point(1.0, 0.0)
        c = R2Point(0.0, 1.0)
        m = Deq()
        m.push_first(b)
        m.push_first(a)
        m.push_last(c)

        Figure.fixed_triangle = m
        self.f = Segment(R2Point(0.0, 0.0), R2Point(1.0, 0.0))

    # Двуугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Segment (двуугольник)
    def test_segment(self):
        assert isinstance(self.f, Segment)

    # Периметр двуугольника равен удвоенной длине отрезка
    def test_perimeter(self):
        assert self.f.perimeter() == approx(2.0)

    # Площадь двуугольника нулевая
    def test_area(self):
        assert self.f.area() == 0.0

    # При добавлении точки двуугольник может не измениться
    def test_add1(self):
        assert self.f.add(R2Point(0.5, 0.0)) is self.f

    # Он не изменяется в том случае, когда добавляемая точка совпадает
    # с одним из концов отрезка
    def test_add2(self):
        assert self.f.add(R2Point(0.0, 0.0)) is self.f

    # При добавлении точки правее двуугольник может превратиться в другой
    # двуугольник
    def test_add3(self):
        assert isinstance(self.f.add(R2Point(2.0, 0.0)), Segment)

    # При добавлении точки левее двуугольник может превратиться в другой
    # двуугольник
    def test_add4(self):
        assert isinstance(self.f.add(R2Point(-1.0, 0.0)), Segment)

    # При добавлении точки двуугольник может превратиться в треугольник
    def test_add5(self):
        assert isinstance(self.f.add(R2Point(0.0, 1.0)), Polygon)

    # Функция `g` вычисляется корректно
    def test_count_points_1(self):
        assert self.f.g() == 2

    def test_count_points_2(self):
        self.f = Segment(R2Point(0.0, 0.0), R2Point(5.0, 0.0))
        assert self.f.g() == 1

    def test_count_points_3(self):
        self.f = Segment(R2Point(6.0, 6.0), R2Point(5.0, 0.0))
        assert self.f.g() == 0

    def test_count_points_4(self):
        self.f = Segment(R2Point(6.0, 6.0), R2Point(1.1, -0.1))
        assert self.f.g() == 0

    def test_count_points_5(self):
        self.f = Segment(R2Point(-0.5, 0.5), R2Point(1.0, 1.0))
        assert self.f.g() == 0


class TestPolygon1:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        Figure._count = 0
        a = R2Point(0.0, 0.0)
        b = R2Point(1.0, 0.0)
        c = R2Point(0.0, 1.0)
        m = Deq()
        m.push_first(b)
        m.push_first(a)
        m.push_last(c)

        Figure.fixed_triangle = m
        self.f = Polygon(
            R2Point(
                0.0, 0.0), R2Point(
                1.0, 0.0), R2Point(
                0.0, 1.0))

    # Многоугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Polygon (многоугольник)
    def test_polygon1(self):
        assert isinstance(self.f, Polygon)

    # Изменение порядка точек при создании объекта всё равно порождает Polygon
    def test_polygon2(self):
        self.f = Polygon(
            R2Point(
                0.0, 1.0), R2Point(
                1.0, 0.0), R2Point(
                0.0, 0.0))
        assert isinstance(self.f, Polygon)

    # Изменение количества вершин многоугольника
    #   изначально их три
    def test_vertexes1(self):
        assert self.f.points.size() == 3

    #   добавление точки внутрь многоугольника не меняет их количества
    def test_vertexes2(self):
        assert self.f.add(R2Point(0.1, 0.1)).points.size() == 3

    #   добавление другой точки может изменить их количество
    def test_vertexes3(self):
        assert self.f.add(R2Point(1.0, 1.0)).points.size() == 4

    #   изменения выпуклой оболочки могут и уменьшать их количество
    def test_vertexes4(self):
        assert self.f.add(
            R2Point(
                0.4,
                1.0)).add(
            R2Point(
                1.0,
                0.4)).add(
                    R2Point(
                        0.8,
                        0.9)).add(
                            R2Point(
                                0.9,
                                0.8)).points.size() == 7
        assert self.f.add(R2Point(2.0, 2.0)).points.size() == 4

    # Изменение периметра многоугольника
    #   изначально он равен сумме длин сторон
    def test_perimeter1(self):
        assert self.f.perimeter() == approx(2.0 + sqrt(2.0))

    #   добавление точки может его изменить
    def test_perimeter2(self):
        assert self.f.add(R2Point(1.0, 1.0)).perimeter() == approx(4.0)

    # Изменение площади многоугольника
    #   изначально она равна (неориентированной) площади треугольника
    def test_area1(self):
        assert self.f.area() == approx(0.5)

    #   добавление точки может увеличить площадь
    def test_area2(self):
        assert self.f.add(R2Point(1.0, 1.0)).area() == approx(1.0)

    # Функция `g` вычисляется корректно для треугольника
    def test_count_points_1(self):
        t = Segment(R2Point(-1.0, 0.0), R2Point(1.0, 0.0))
        t = t.add(R2Point(0.0, 1.0))
        assert t.g() == 2

    # Функция `g` вычисляется корректно для квадрата
    def test_count_points_2(self):
        t = Segment(R2Point(-1.5, 0.0), R2Point(1.5, 0.0))
        t = t.add(R2Point(0.0, 1.5))
        t = t.add(R2Point(0.0, -1.5))
        assert t.g() == 0

    # Функция `g` вычисляется корректно для трапеции
    def test_count_points_3(self):
        t = Segment(R2Point(-1.0, 0.0), R2Point(1.0, 0.0))
        t = t.add(R2Point(0.0, 1.0))
        t = t.add(R2Point(0.0, -1.0))
        t = t.add(R2Point(1.0, 1.0))
        assert t.g() == 2

    # Функция `g` вычисляется корректно для прямоугольника
    def test_count_points_4(self):
        t = Segment(R2Point(-1.0, 0.0), R2Point(1.0, 0.0))
        t = t.add(R2Point(0.0, 1.0))
        t = t.add(R2Point(0.0, -1.0))
        t = t.add(R2Point(1.0, 1.0))
        t = t.add(R2Point(1.0, -1.0))
        t = t.add(R2Point(-1.0, 1.0))
        t = t.add(R2Point(-1.0, -1.0))
        assert t.g() == 0

    # Функция `g`
    # вычисляется корректно для большой трапеции
    def test_count_points_5(self):
        t = Segment(R2Point(-1.0, 0.0), R2Point(1.0, 0.0))
        t = t.add(R2Point(0.0, 1.0))
        t = t.add(R2Point(0.0, -1.0))
        t = t.add(R2Point(1.0, 1.0))
        t = t.add(R2Point(1.0, -1.0))
        t = t.add(R2Point(-1.0, 1.0))
        t = t.add(R2Point(-1.0, -1.0))
        t = t.add(R2Point(3.0, -1.0))
        assert t.g() == 0

    # Функция `g`
    # вычисляется корректно для большого треугольника
    def test_count_points_6(self):
        t = Segment(R2Point(-1.0, 0.0), R2Point(1.0, 0.0))
        t = t.add(R2Point(0.0, 1.0))
        t = t.add(R2Point(0.0, -1.0))
        t = t.add(R2Point(1.0, 1.0))
        t = t.add(R2Point(1.0, -1.0))
        t = t.add(R2Point(-1.0, 1.0))
        t = t.add(R2Point(-1.0, -1.0))
        t = t.add(R2Point(3.0, -1.0))
        t = t.add(R2Point(-1.0, 3.0))
        assert t.g() == 0

    def test_count_points_7(self):
        t = Segment(R2Point(-0.5, 0.5), R2Point(0.5, 0.0))
        t = t.add(R2Point(1.0, 1.0))
        t = t.add(R2Point(0.0, -0.5))
        t = t.add(R2Point(0.5, 0.5))
        t = t.add(R2Point(0.5, -1.0))
        assert t.g() == 0


class TestPolygon2:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        Figure._count = 0
        a = R2Point(-5.0, 3.0)
        b = R2Point(5.0, 3.0)
        c = R2Point(-2.0, 8.0)
        m = Deq()
        m.push_first(b)
        m.push_first(a)
        m.push_last(c)

        Figure.fixed_triangle = m
        self.f = Polygon(
            R2Point(
                0.0, 0.0), R2Point(
                1.0, 0.0), R2Point(
                0.0, 1.0))

    def test_count_points_1(self):
        t = Segment(R2Point(-3.0, 4.0), R2Point(-2.0, 5.0))
        t = t.add(R2Point(-2.0, 6.0))
        assert t.g() == 3

    def test_count_points_2(self):
        t = Segment(R2Point(-3.0, 4.0), R2Point(-2.0, 5.0))
        t = t.add(R2Point(-2.0, 6.0))
        t = t.add(R2Point(-9.0, -1.5))
        assert t.g() == 3

    def test_count_points_3(self):
        t = Segment(R2Point(-3.0, 4.0), R2Point(-2.0, 5.0))
        t = t.add(R2Point(-2.0, 6.0))
        t = t.add(R2Point(-9.0, -1.5))
        t = t.add(R2Point(1.0, 4.0))
        assert t.g() == 2

    def test_count_points_4(self):
        t = Segment(R2Point(-3.0, 4.0), R2Point(-2.0, 5.0))
        t = t.add(R2Point(-2.0, 6.0))
        t = t.add(R2Point(-9.0, -1.5))
        t = t.add(R2Point(1.0, 4.0))
        t = t.add(R2Point(1.0, 8.0))
        assert t.g() == 2

    def test_count_points_5(self):
        t = Segment(R2Point(-3.0, 4.0), R2Point(-2.0, 5.0))
        t = t.add(R2Point(-2.0, 6.0))
        t = t.add(R2Point(-9.0, -1.5))
        t = t.add(R2Point(1.0, 4.0))
        t = t.add(R2Point(1.0, 8.0))
        t = t.add(R2Point(-2.0, 8.0))
        assert t.g() == 2

    def test_count_points_6(self):
        t = Segment(R2Point(-3.0, 4.0), R2Point(-2.0, 5.0))
        t = t.add(R2Point(-2.0, 6.0))
        t = t.add(R2Point(-9.0, -1.5))
        t = t.add(R2Point(1.0, 4.0))
        t = t.add(R2Point(1.0, 8.0))
        t = t.add(R2Point(-2.0, 8.0))
        t = t.add(R2Point(-3.0, 7.0))
        assert t.g() == 2
