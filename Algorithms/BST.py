from Data_Structures.BinaryTreeClass import TreeNode

def inOrder(root):
    if(root==None): return []
    L=inOrder(root.left)
    R=inOrder(root.right)

    return L+[root.val]+R

def is_BST(root):
    if(root==None): return True,-float('inf'),float('inf')
    
    isL,maxL,minL=is_BST(root.left)
    isR,maxR,minR=is_BST(root.right)

    if(isL and isR):
        if(maxL < root.val and minR > root.val):
            return True,max(maxR,root.val),min(minL,root.val)

    return False,-float('inf'),float('inf')


def search_BST(root,target):
    if(root==None): return False
    if(root.val == target): return True
    elif(root.val < target): return search_BST(root.right,target)
    return search_BST(root.left,target)


def insert_BST(root,ele):
    if(root==None): return ele
    if(ele.val == root.val): return root
    if(ele.val > root.val):
        R=insert_BST(root.right,ele)
        root.right=R
    else:
        L=insert_BST(root.left,ele)
        root.left=L
    return root


def delete_BST(root,target):
    if(root==None): return None

    if(root.val == target):
        if(root.left == None): return root.right
        elif(root.right == None): return root.left
        else:
            L=root.left
            if(L.left==None):
                root.val=root.left.val
                root.left=root.left.right
                return root

            while(L.left.left!=None):
                L=L.left
            root.val=L.left.val
            L.left=None
            return root
            
    elif(root.val > target):
        L=delete_BST(root.left,target)
        root.left=L
    else:
        R=delete_BST(root.right,target)
        root.right=R
    return root

def delete_BST(root,target):
    if(root==None): return None

    if(root.val == target):
        if(root.left == None): return root.right
        elif(root.right == None): return root.left
        else:
            L=root.left
            if(L.right==None):
                L.right=root.right
                return L

            while(L.right.right!=None):
                L=L.right
            root.val=L.right.val
            L.right=L.right.left
            return root
            
    elif(root.val > target):
        L=delete_BST(root.left,target)
        root.left=L
    else:
        R=delete_BST(root.right,target)
        root.right=R
    return root

def is_balanced(root):
    if(root == None): return True,0
    isL,l=is_balanced(root.left)
    isR,r=is_balanced(root.right)

    if(isL and isR and abs(l-r)<=1):
        return True,1+max(l,r)
    return False,1+max(l,r)


def Helper(lst,left,right):
    if(left>right): return None

    mid=left+(right-left)//2
    #print(lst[mid]) 
    root=TreeNode(lst[mid])
    root.left=Helper(lst,left,mid-1)
    root.right=Helper(lst,mid+1,right)

    return root


def Sorted_array_to_balanced_BST(lst):
    return Helper(lst,0,len(lst)-1)




# Constructing Tree Manually

root = TreeNode(10)
root.left = TreeNode(8)
root.left.left = TreeNode(3)
root.right = TreeNode(13)
root.right.left = TreeNode(11)
root.right.right = TreeNode(17)
root.right.left.right = TreeNode(12)
root.right.right.left = TreeNode(16)
root.right.right.right = TreeNode(31)

ele=TreeNode(1)

root = insert_BST(root,ele)

print(search_BST(root,17))
delete_BST(root,10)
print("Balanced : ",is_balanced(root))

lst = [1,2,3,4,5,6,7,8,9,10]

node = Sorted_array_to_balanced_BST(lst)


arr = inOrder(node)
print("inOrder of Balanced BST ",arr)
