def f1(x):
    return x&(x+1)

def f2(x):
    return x|(x+1)

class Fenwick:
    def __init__(self, array):
        if array is None:
            self.under = []
            self.array = []
            self.length=0
        else:
            self.under = array
            self.array = []
            for i in range(len(array)):
                self.array.append(sum(self.under[f1(i):i])+self.under[i])
            self.length = len(array)

    #self.under - обычный массив, self.array - массив Фенвика

    def sum(self, l, r):
        s=0
        l-=1 #чтобы сумма включала левую границу
        while r>=0:
            s+=self.array[r]
            r=f1(r)-1
        while l>=0:
            s-=self.array[l]
            l=f1(l)-1
        return s


    def update(self, number, newvalue):
        d = newvalue-self.under[number]
        self.under[number] = newvalue
        while number<len(self.array):
            self.array[number]=self.array[number]+d
            number = number|(number+1)

    def add(self, value):
        self.under.append(value)
        self.array.append(sum(self.under[f1(self.length):self.length])+self.under[self.length])
        self.length+=1

    def search(self, value):
        return False if self.under.count(value)==0 else True

    def searchinfenwick(self, value):
        return False if self.array.count(value)==0 else True

    def remove(self,value):
        if self.search(value) is False:
            return
        for i in range(self.length):
            if self.under[-i-1]==value:
                number = self.length-i-1
                break
        h = self.under[::-1]
        h.remove(value)
        self.under = h[::-1]
        self.array.pop(-1)
        self.length-=1
        for i in range(number,self.length):
            self.array[i]=sum(self.under[f1(i):i])+self.under[i]

empty=Fenwick(None)
for i in range(4):
    empty.add(i+1)
    print(empty.search(3))
    print(empty.searchinfenwick(3))
    print(empty.under, empty.array)
    print(empty.sum(0,i))
for i in range(2):
    empty.remove(i+1)
    print(empty.search(3))
    print(empty.searchinfenwick(3))
    print(empty.under, empty.array)
    print(empty.sum(0,1))
print('\n')
a=[1,2,3,4,5,6,7,8]
f=Fenwick(a)
print(f.under,f.array, f.sum(0,f.length-1))
print(f.search(7))
print(f.search(1))
f.update(0,0)
f.remove(7)
f.remove(8)
print(f.search(7))
print(f.search(1))
print(f.under,f.array, f.sum(0,f.length-1))
f.add(10)
print(f.under,f.array, f.sum(0,f.length-1))
print(f.sum(2,5))