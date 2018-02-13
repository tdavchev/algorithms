class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, data):
        self.left = data

    def set_right(self, data):
        self.right = data

# merge(fuse) two sorted linked lists
def concatenate_lists(head1, head2):
    
    if head1 == None:
      return head2

    if head2 == None:
        return head1
    
    # use left for previous.
    # use right for next.
    tail1 = head1.left
    tail2 = head2.left
    
    tail1.right = head2
    head2.left = tail1
    
    head1.left = tail2
    tail2.right = head1
    return head1

def convert_to_linked_list(root):
    
    if root == None:
        return None
    
    list1 = convert_to_linked_list(root.left)
    list2 = convert_to_linked_list(root.right)
    
    root.left = root.right = root
    result = concatenate_lists(list1, root)
    result = concatenate_lists(result, list2)
    
    return result

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


ans = convert_to_linked_list(root)

while ans !=