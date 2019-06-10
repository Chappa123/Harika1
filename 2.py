import random
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sorted_array_to_bst(nums):
    
    if not nums:
        return None
    mid_val = len(nums)//2
    node = TreeNode(nums[mid_val])
    node.left = sorted_array_to_bst(nums[:mid_val])
    node.right = sorted_array_to_bst(nums[mid_val+1:])
    return node
def preOrder(node): 
    if not node: 
        return      
    print(node.val)
    preOrder(node.left) 
    preOrder(node.right)   

arr = [] 
for j in range(10): 
    arr.append(random.randint(1, 100)) 
print("10 random numbers:",arr) 
arr.sort()
print("After sorting:", arr)   

result = sorted_array_to_bst(arr)
print("Preorder of the resultant balanced BST")
preOrder(result)
