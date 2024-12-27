class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

    def __repr__(self):
        return f"BinaryTreeNode({self.val})"

    def __str__(self):
        return f"BinaryTreeNode with value {self.val}"
