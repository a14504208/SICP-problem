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

def midpoint(p1, p2):
    """
    Return midpoint between p1 and p2
    """
    
    x1, y1 = p1.x(), p1.y()
    x2, y2 = p2.x(), p2.y()

    return Point((x1 + x2)/2, (y1 + y2)/2)

def midpoint_segment(line):
    """
    Return midpoint of the Segment line
    """
    return midpoint(line.start(), line.end())
              
if __name__ == '__main__':
    a = Point(3, 5)
    b = Point(4, 6)
    print(a, b, sep=', ')
    line = Segment(a, b)
    print(line)
