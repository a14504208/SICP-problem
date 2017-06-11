class Point:
    def __init__(self, x, y):
        self.coordinate = (x, y)

    def x(self):
        return self.coordinate[0]

    def y(self):
        return self.coordinate[1]

    def __str__(self):
        return '({0}, {1})'.format(self.x(), self.y())

    def __repr__(self):
        return 'Point({0}, {1})'.format(self.x(), self.y())

class Segment:
    def __init__(self, start, end):
        self.start_point = start
        self.end_point = end

    def start(self):
        return self.start_point

    def end(self):
        return self.end_point

    def __str__(self):
        return '{0} -> {1}'.format(self.start(), self.end())

    def __repr__(self):
        return 'Segment({0}, {1})'.format(repr(self.start()), repr(self.end()))
              
if __name__ == '__main__':
    a = Point(3, 5)
    b = Point(4, 6)
    print(a, b, sep=', ')
    line = Segment(a, b)
    print(line)
