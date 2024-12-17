n = int(input())
a = list(map(int, input().split()))
l=len(a)
class Note:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class Tree:
    def __init__(self):
        self.root = None
    def add(self,value):
        if self.root == None:
            self.root = Note(value)
            return
        t = self.root
        parent = None
        while t != None:
            if value < t.value:
                parent = t
                t = t.left
            elif value > t.value:
                parent = t
                t = t.right
            else:
                return
        New = Note(value)
        New.parent=parent
        if value < parent.value:
            parent.left = New
        else:
            parent.right = New

    def search(self,value):
        t = self.root
        while t != None and t.value != value:
            if value < t.value:
                t = t.left
            else:
                t = t.right
        return False if t==None else True

    def ifleaf(self,value):
        t = self.root
        while t.value != value:
            if value < t.value:
                t = t.left
            else:
                t = t.right
        if t.left==None and t.right==None:
            return True
        else:
            return False

derevo=Tree()
for i in range(l):
    derevo.add(a[i])
b=[]
for value in a:
    if derevo.ifleaf(value)==True and b.count(value)==0:
        b.append(value)
def qsort(b):
    if len(b)<=1:
        return b
    m=b[len(b)//2]
    low = [n for n in b if n<m]
    equal = [n for n in b if n==m]
    high = [n for n in b if n>m]
    return qsort(low)+equal+qsort(high)

c=qsort(b)
for i in range(len(c)):
    print(c[i], end=' ')