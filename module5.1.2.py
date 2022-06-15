import math

class Object:

    def __init__(self, area=None, perimeter=None):
        self.area = area
        self.perimeter = perimeter    

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Foursquare(Object):

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d              
        self.ab = self.sides()[0] 
        self.bc = self.sides()[1]
        self.cd = self.sides()[2]
        self.da = self.sides()[3]
        self.perimeter = self.ab + self.bc + self.cd + self.da
                        
    def sides(self):
        x1 = self.a.x
        y1 = self.a.y
        x2 = self.b.x
        y2 = self.b.y
        x3 = self.c.x
        y3 = self.c.y
        x4 = self.d.x
        y4 = self.d.y
        self.area = ((x1*y2 + x2*y3 + x3*y4 + x4*y1)-(y1*x2 + y2*x3 + y3*x4 + y4*x1))/2
        if (x1*y2 + x2*y3 + x3*y4 + x4*y1) < (y1*x2 + y2*x3 + y3*x4 + y4*x1):
            self.area = ((y1*x2 + y2*x3 + y3*x4 + y4*x1)-(x1*y2 + x2*y3 + x3*y4 + x4*y1))/2
            
        ab = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        bc = math.sqrt((x3-x2)**2 + (y2-y3)**2)
        cd = math.sqrt((x4-x3)**2 + (y4-y3)**2)
        da = math.sqrt((x4-x1)**2 + (y4-y1)**2)
        return ab, bc, cd, da

    

if __name__ == '__main__':
    a = Point(4, 2)
    b = Point(7, 4)
    c = Point(5, 7)
    d = Point(0, 6)
    f = Foursquare(a, b, c, d)

    print('Side ab: ', float('%.3f'%(f.ab)))
    print('Side bc: ', float('%.3f'%(f.bc)))
    print('Side cd: ', float('%.3f'%(f.cd)))
    print('Side da: ', float('%.3f'%(f.da)))
    print('Perimeter = ', float('%.3f'%(f.perimeter)))
    print('Area = ', float('%.3f'%(f.area)))
    
