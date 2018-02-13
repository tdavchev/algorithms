class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_right(self, data):
        self.right = data

    def set_left(self, data):
        self.left = data

def height(root):
    if root == None:
        return 0

    stack = []
    while root != None:
        stack.append(root)
        root = root.left

    count = len(stack)
    while len(stack) > 0:
        ele = stack.pop()
        if ele.right != None:
            ele = ele.right
            while ele != None:
                stack.append(ele)
                ele = ele.left

            if count < len(stack) + 1:
                count = len(stack) + 1

    return count
    

def find_diameter(root):
    if root == None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    # ldiameter = find_diameter(root.left)
    # rdiameter = find_diameter(root.right)

    return max(lheight + rheight + 1, max(ldiameter, rdiameter))

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(root, diameter):
            if not root: return 0, diameter
            left, diameter = depth(root.left, diameter)
            right, diameter = depth(root.right, diameter)
            return 1 + max(left, right), max(diameter, 1 + left + right)
            
        return depth(root, 1)[1] - 1

def depth(root, diameter):
    if not root: return 0, diameter

    left, diameter = depth(root.left, diameter)
    right, diameter = depth(root.right, diameter)
    
    return 1 + max(left, right), max(diameter, 1 + left + right)

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
ele10 = TreeNode(11)
ele11 = TreeNode(12)
ele12 = TreeNode(13)
ele13 = TreeNode(14)
ele14 = TreeNode(15)
ele15 = TreeNode(16)
ele16 = TreeNode(17)

root.set_left(ele1)
root.set_right(ele4)
ele1.set_left(ele2)
ele1.set_right(ele3)
ele4.set_left(ele5)
ele4.set_right(ele6)
ele6.set_left(ele7)
ele7.set_left(ele8)
ele8.set_left(ele9)
ele8.set_right(ele10)
ele10.set_right(ele11)
ele11.set_left(ele12)
ele6.set_right(ele13)
ele13.set_right(ele14)
ele14.set_left(ele15)
ele15.set_right(ele16)

s = Solution()
ans = s.diameterOfBinaryTree(root)
# ans = find_diameter(root)
print(ans)