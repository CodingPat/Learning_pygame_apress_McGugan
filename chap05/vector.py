import math

class Vector2:
    
    def __init__(self,x=0,y=0):
        self.x=x;
        self.y=y;
        
        
    def __str__(self):
        return "({},{})".format(self.x,self.y)
    
    @staticmethod
    def from_points(P1,P2):
        return Vector2(P2[0]-P1[0],P2[1]-P1[1])
    
    def get_magnitude(self):
        return math.sqrt(self.x**2+self.y**2)
        
    def normalize(self):
        magnitude=self.get_magnitude()
        self.x/=magnitude
        self.y/=magnitude
    
    def __add__(self,other):
        return Vector2(self.x+other.x,self.y+other.y)
    
    def __sub__(self,other):
        return Vector2(self.x-other.x,self.y-other.y)
    
    def __neg__(self):
        return Vector2(-self.x,-self.y)
    
    def __mul__(self,scalar):
        return Vector2(self.x*scalar,self.y*scalar)
    
if __name__=='__main__':
    A=(10.0,20.0)
    B=(30.0,35.0)
    C=(15.0,45.0)
    AB=Vector2.from_points(A,B)
    print("Vector AB is :",AB)
    
    BC=Vector2.from_points(B,C)
    print("Vector BC is :",BC)
    
    AC=Vector2.from_points(A,C)
    print("Vector AC is :",AC)
    
    AC=AB+BC
    print("Vector AB+AC is :",AC)
    
    print("Going from A to B in 10 steps")
    step=AB*0.1
    position=Vector2(A[0],A[1])
    for n in range(10):
        position+=step
        print(position)
    
     
        