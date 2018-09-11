class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, data):
        self.left = data

    def set_right(self, data):
        self.right = data

    def hasNext(self):
        if self != None:
            return True

        return False

    def getNext(self, which):
        if which == "left":
            return self.left
        elif which == "right":
            return self.right

        return None

    def inorder_traverse(self):
        if self.data == None:
            return None

        stck = []
        while len(stck) != 0 or self != None:
            while self != None:
                stck.append(self)
                self = self.left

            self = stck.pop()
            print(self.data)
            self = self.right

    def inorder_successor(self, of):
        if self.data == None:
            return None

        stck = []
        next_ = False
        while len(stck) != 0 or self != None:
            while self != None:
                stck.append(self)
                self = self.left

            self = stck.pop()
            if next_:
                print(self.data)
                return

            if self.data == of:
                next_ = True

            self = self.right


def identical(root1, root2):
    if root1 == None and root2 == None:
        return True

    if (root1 == None and root2 != None) or root1 != None and root2 == None:
        return False

    if root1.data != root2.data:
        return False


    return identical(root1.left, root2.left) and identical(root1.right, root2.right)


root1 = TreeNode(100)
ele1 = TreeNode(50)
ele2 = TreeNode(25)
ele3 = TreeNode(75)
ele4 = TreeNode(10)
ele5 = TreeNode(15)
ele6 = TreeNode(200)
ele7 = TreeNode(300)
ele8 = TreeNode(350)


root1.set_left(ele1)
root1.set_right(ele6)
ele1.set_left(ele2)
ele1.set_right(ele3)
ele2.set_left(ele4)
ele4.set_right(ele5)
ele6.set_right(ele7)
ele7.set_right(ele8)

root2 = TreeNode(100)
ele1 = TreeNode(50)
ele2 = TreeNode(25)
ele3 = TreeNode(75)
# ele4 = TreeNode(10)
# ele5 = TreeNode(15)
ele6 = TreeNode(200)
ele7 = TreeNode(125)
ele8 = TreeNode(350)


root2.set_left(ele1)
root2.set_right(ele6)
ele1.set_left(ele2)
ele1.set_right(ele3)
# ele2.set_left(ele4)
# ele4.set_right(ele5)
ele6.set_left(ele7)
ele6.set_right(ele8)

print(identical(root1, root2))
print("--------")
root1.inorder_traverse()
print("--------")
root2.inorder_successor(350)