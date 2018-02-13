class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, data):
        self.left = data

    def set_right(self, data):
        self.right = data

def create_minimal_bst(arr, start, end):
    if end < start:
        return None

    mid = start + (end - start)//2
    print("so I am here now ,,, and mid is ,,, ", mid)
    # print(mid)
    n = TreeNode(arr[mid])
    print(n.data)
    print("setting its left to the arr in indexes", (start, mid-1))
    print("setting its right to the arr in indexes", (mid+1, end))

    n.left = create_minimal_bst(arr, start, mid-1)
    n.right = create_minimal_bst(arr, mid+1, end)

    print("thats it for this one folks ....", n.data)
    print("with children ....")
    if n.left != None:
        print("left ", n.left.data)
    if n.right != None:
        print("right ", n.right.data)
    print("------------------------------------------")

    return n

def create_bst(arr):
    return create_minimal_bst(arr, 0, len(arr)-1)

arr = [1,2,3,4,5]
ans = create_bst(arr)

