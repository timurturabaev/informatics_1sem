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
            else:
                parent = t
                t = t.right

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

    def remove(self,value):
        t = self.root
        while t != None and t.value != value:
            if value < t.value:
                t = t.left
            else:
                t = t.right

        if t==None:
            return

        if t.left == None and t.right == None:
            if t == parent.left:
                t.parent.left = None
            else:
                parent.right = None
            return

        if t.left == None or t.right == None:
            child = t.left if t.left != None else t.right
            if child.value >= parent:
                parent.right = child
            else:
                parent.left = child
            return

        successor = t.right
        while successor.left != None:
            successor = successor.left
        if successor == t.right:
            successor.right.parent = successor.parent
            successor.parent.left = successor.right
            successor.right = t.right
            successor.right.parent = successor

        successor.parent = t.parent
        successor.left = t.left

        successor.parent.left = successor
        successor.left.parent = successor

T = Tree()
T.add(6)
T.add(-1)
T.add(4)
T.add(7)
T.add(3)
print(T.search(-1))
T.remove(-1)
print(T.search(-1))