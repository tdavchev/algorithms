class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, data):
        self.left = data

    def set_right(self, data):
        self.right = data

def level_order_traversal(root, dicto, level):
    if root == None:
        return dicto

    if level in dicto.keys():
        dicto[level].append(root.data)
    else:
        dicto[level] = [root.data]

    dicto = level_order_traversal(root.left, dicto, level+1)
    dicto = level_order_traversal(root.right, dicto, level+1)

    return dicto

from collections import deque

def level_order_traversal2(root):
    if root == None:
        return

    queues = [deque(), deque()]

    current_queue = queues[0]
    next_queue = queues[1]

    current_queue.append(root)
    level_number = 0

    while current_queue:
        temp = current_queue.popleft()
        print(temp.data)

        if temp.left != None:
            next_queue.append(temp.left)

        if temp.right != None:
            next_queue.append(temp.right)

        if not current_queue:
            print()
            level_number += 1
            current_queue = queues[level_number % 2]
            next_queue = queues[(level_number + 1) % 2]

    print()

def level_order_traversal3(root):
    if root == None:
        return None

    current_queue = deque()
    current_queue.append(root)
    current_queue.append(None)

    while len(current_queue) != 0:
        temp = current_queue.popleft()
        print(str(temp.data))
        if temp.left != None:
            current_queue.append(temp.left)

        if temp.right != None:
            current_queue.append(temp.right)

        if current_queue[0] == None:
            print()
            current_queue.popleft()

            if len(current_queue) != 0:
                current_queue.append(None)

    print()

root = TreeNode(100)
ele1 = TreeNode(50)
ele2 = TreeNode(25)
ele3 = TreeNode(75)
ele4 = TreeNode(200)
ele5 = TreeNode(125)
ele6 = TreeNode(350)

root.set_left(ele1)
root.set_right(ele4)
ele1.set_left(ele2)
ele1.set_right(ele3)
ele4.set_left(ele5)
ele4.set_right(ele6)

# ans = level_order_traversal(root, {}, 1)

# print(ans)

level_order_traversal3(root)