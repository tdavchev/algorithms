class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_right(self, data):
        self.right = data

    def set_left(self, data):
        self.left = data

def print_left_perimeter(root):
  while root != None:
    curr_val = root.data

    if root.left != None:
      root = root.left
    elif root.right != None:
      root = root.right
    else: # leaf node
      break
    print(str(curr_val) + " ")

def print_right_perimeter(root):
  r_values = [] # stack for right side values.

  while root != None:
    curr_val = root.data

    if root.right != None:
      root = root.right
    elif root.left != None:
      root = root.left
    else: # leaf node
      break
    r_values.append(curr_val)

  while len(r_values) != 0:
    print(str(r_values.pop()) + " ")

def print_leaf_nodes(root):
  if root != None:
    print_leaf_nodes(root.left)

    if root.left == None and root.right == None:
      print(str(root.data) + " ")

    print_leaf_nodes(root.right)

def display_tree_perimeter(root):
  if root != None:
    print("------")
    print(str(root.data) + " ")

    print_left_perimeter(root.left)

    print(str(root.data) + " ")
    print("------")
    if root.left != None or root.right != None:
      print_leaf_nodes(root)

    print(str(root.data) + " ")
    print("------")
    print_right_perimeter(root.right)

root = TreeNode(1)
ele1 = TreeNode(2)
ele2 = TreeNode(3)
ele3 = TreeNode(4)
ele4 = TreeNode(5)
ele5 = TreeNode(6)
ele6 = TreeNode(7)
ele7 = TreeNode(8)
ele8 = TreeNode(9)
ele9 = TreeNode(10)


root.set_left(ele1)
root.set_right(ele2)

ele1.set_left(ele3)
ele1.set_right(ele4)
ele3.set_left(ele8)
ele4.set_right(ele7)
ele2.set_right(ele6)
ele6.set_right(ele9)

display_tree_perimeter(root)