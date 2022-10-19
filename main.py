from math import sqrt


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, p):
        return sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)

    def abs(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
      return f"({self.x}, {self.y})"


class Rectangle:
  
    def __init__(self, p1, p2):
      self.p1 = Point(p1.x,p1.y)
      self.p2 = Point(p2.x,p2.y)

    def area(self):
      return abs((self.p1.x-self.p2.x) * (self.p1.y-self.p2.y))

    def center(self):
      center = Point((self.p1.x+self.p2.x)/2, (self.p1.y+self.p2.y)/2)
      return center


def main():
    p1 = Point(3.0, 4.0)
    print(f"The point ({p1.x}, {p1.y}) is at a distance of {p1.abs()} from the origin.")

    p2 = Point(-1.0, 6.5)
    print(f"It is a distance {p1.dist_to(p2):.5} away from the point ({p2.x}, {p2.y}).")

    r1 = Rectangle(p1,p2)
    print(f"the area of the rectangle represented by these points is {r1.area()}, and the center point is {r1.center()}")
  

if __name__ == "__main__":
    main()
