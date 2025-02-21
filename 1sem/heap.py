class Heap:
    
    def __init__(self, a):
        self.array = a
        for i in range(len(self.array)//2, -1, -1):
            self.siftDown(i)
    
    def siftDown(self, i):
        while 2 * i + 1 < len(self.array):
            max_child_index = 2 * i + 1
            if 2 * i + 2 < len(self.array) and self.array[2 * i + 1] < self.array[2 * i + 2]:
                max_child_index = 2 * i + 2
            if self.array[i] > self.array[max_child_index]:
                break
            self.array[i], self.array[max_child_index] = self.array[max_child_index], self.array[i]
            i = max_child_index
        return
    
    def siftUp(self, i):
        while self.array[i] > self.array[(i - 1) // 2] and i > 0:
            self.array[i], self.array[(i - 1) // 2] = self.array[(i - 1) // 2], self.array[i]
            i = (i - 1) // 2
        return
    
    def add(self, value):
        self.array.append(value)
        self.siftUp(len(self.array) - 1)
    
    def pop(self):
        result = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.siftDown(0)
        return result

n, k = list(map(int, input().split()))
h = Heap([])
for element in list(map(int, input().split())):
    # Этот цикл напишете сами
    pass
h.array.sort()
print(" ".join(map(str, h.array)))
