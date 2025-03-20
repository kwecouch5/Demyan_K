class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        s = f' Координата по x={self.x}, Координата по y={self.y}'
        return s
    def move_00(self):
        self.x=0
        self.y=0
    def distance(self,point_a):
        s = ((self.x-point_a.x)**2+(self.y-point_a.y)**2)**0.5
        print(s)
        return s
    def move(self,x_1,y_1):
        self.x=x_1
        self.y=y_1

a=Point(1,1)
b=Point(0,0)
a.distance(b)
print(a)
a.move_00()
print(a)