class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return "Node = {}".format(self.val)
class Solution:
    def diameterOfBinaryTree(self, root):
        if root == None:
            return 0
        left_height = self.max_tree_height(root.left)
        right_height = self.max_tree_height(root.right)
        return max(left_height + right_height,\
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right))
    def max_tree_height(self, node):
        if node == None:
            return 0
        return max(self.max_tree_height(node.right) + 1, self.max_tree_height(node.left) + 1)

def main():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    print(Solution().diameterOfBinaryTree(a))

if __name__ == '__main__':
    main()
