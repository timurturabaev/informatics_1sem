class Vector():
    def __init__(self, x, y, z):
        assert isinstance(x, int) or isinstance(y, int) or isinstance(z, int) or isinstance(x, float) or isinstance(y, float) or isinstance(z, float)
        self.x = x
        self.y = y
        self.z = z
    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x*other.x+self.y*other.y+self.z*other.z
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other, self.z * other)
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x + other, self.y + other, self.z + other)
    def __radd__(self, other):
        print('error')
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x - other, self.y - other, self.z - other)
    def __rsub__(self, other):
        return None
    def __str__(self):
        return f'({self.x},{self.y},{self.z})'
n=int(input('Число точек: '))
v = Vector(0,0,0)
for i in range(n):
    print('Координаты',i+1,'точки: ', end='')
    a=input().split()
    x=int(a[0])
    y=int(a[1])
    z=int(a[2])
    w=Vector(x,y,z)
    v=v+w
print('Центр масс:',v*(1/n))