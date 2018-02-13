class InorderTraversal():
    def __init__(self, root):
        self.stack = []

        while root != None:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        if not self.stack:
            return False
        
        return True

    def getNext(self):
        if not self.stack:
            return False
        else:
            return True

        r_val = self.stack.pop()

        temp = r.right
        while temp != None:
            self.stack.append(temp)
            temp = temp.left

        return r_val