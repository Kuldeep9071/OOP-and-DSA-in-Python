from Data_Structures.BinaryTreeClass import TreeNode

def preOrder(root,lst):
    if(root==None): return

    lst.append(root.val)
    preOrder(root.left,lst)
    preOrder(root.right,lst)

def postOrder(root,lst):
    if(root==None): return

    postOrder(root.left,lst)
    postOrder(root.right,lst)
    lst.append(root.val)


def inOrder(root,lst):
    if(root==None): return

    inOrder(root.left,lst)
    lst.append(root.val)
    inOrder(root.right,lst)

def height(root):
    if(root==None): return 0
    return 1+max(height(root.left),height(root.right))

def size(root):
    if(root==None): return 0
    return 1+size(root.left)+size(root.right)


# Making Tree Manually

root = TreeNode(2)
root.left = TreeNode(3)
root.left.left=TreeNode(1)
root.right=TreeNode(5)
root.right.left=TreeNode(3)
root.right.right=TreeNode(7)
root.right.left.right=TreeNode(4)
root.right.right.left=TreeNode(6)
root.right.right.right=TreeNode(8)

lst=[]

inOrder(root,lst)
print("In Order : ",lst)
lst=[]
preOrder(root,lst)
print("Pre Order: ",lst)
lst=[]
postOrder(root,lst)
print("Post Order :",lst)

print("Height : ",height(root))
print("Size : ",size(root))

print(repr(root))
print(str(root))
