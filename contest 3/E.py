tests = int(input())
steps = [0]*tests
nums = []
for i in range(tests):
    steps[i]=int(input())
    a = list(map(int, input().split()))
    nums.append(a)

def f(i):
    return i & (i+1)

def matchflags(array):
    flags=[0]
    for i in range(1,len(array)):
        if array[i]>array[i-1] and array[i]>array[i+1]:
            flags.append(1)
        else:
            flags.append(0)
    return flags

def ssum(array,q,b):
    s=0
    for x in range(q,b):
        if array[x]<array[b]:
            s+=array[x]
    return s


class Fenwick:
    def __init__(self):
        self.farray = [0]
    def flagsum(self, array):
        fs=0
        flags=[0]
        lowflag=0
        for h in range(1, len(array) - 1):
            lowflag=0
            if array[h]==array[h - 1]:
                self.farray.append(self.farray[h - 1])
                fs += self.farray[h]
                continue
            for j in range(len(flags)):
                low=[]
                lown=[]
                if array[h]>=array[flags[-j-1]]:
                    low.append(array[flags[-j-1]])
                    lown.append(flags[-j - 1])
            for k in range(len(low)-1):
                if low[k]>low[k+1]:
                    lowflag=low[k]
            if array[h]>array[h - 1] and array[h]>array[h + 1]:
                    flags.append(h)
            self.farray.append(ssum(array, lowflag, h) + self.farray[lowflag])
            fs+=self.farray[h]
        fs+=ssum(array,lowflag,len(array)-1)+self.farray[lowflag]
        return fs

for p in range(tests):
    c=Fenwick()
    print(c.flagsum(nums[p]))