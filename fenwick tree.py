class Element:
    def __init__(self, value, number):
        self.value = value
        self.number = number
        self.next = None
        self.prev = None

class Fenwick:
    def __init__(self):
        self.zero=None
        self.last=None
        self.length=0

    def add(self, value):
        if self.zero==None:
            self.zero = Element(value, 0)
            self.last = Element(value, 0)
            self.length=1
            return
        if self.zero.next==None:
            self.last = Element(value, 1)
            self.zero.next = self.last
            self.last.prev = self.zero
        new = Element(value, self.length)
        new.prev = self.last
        self.last.next = new
        self.last = new
        self.length+=1

    def search(self, value):
        el = self.zero
        t=0
        n=self.last.number
        if el is None:
            return False
        if value==self.last.value:
            return True
        while value!=el.value and t<n:
            el = el.next
        return False if t==n else True
    def removebyvalue(self,value):
        el = self.zero
        if el is None:
            return
        while value != el.value:
            el = el.next
            if el is None:
                return
        if el.number==self.last.number:
            self.last = el.prev
            self.last.next = None
            el = None
            el.next = None
        else:
            elnext = el.next
            for i in range(elnext.number,self.length):
                elnext.number-=1
                elnext = elnext.next
            el.prev.next = el.next
            el.next.prev = el.prev
            el.next = None
            el.prev = None
            el.value = None
            el = None

m=Fenwick()
m.add(1)
m.add(2)
m.add(3)
print(m.last.number)
print(m.search(1))
print(m.search(2))
m.removebyvalue(2)
print(m.search(2))
print(m.last.number)
print(m.search(3))
print(m.length)