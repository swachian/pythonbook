# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root):
        try:
            self.traverse(root)
        except:
            return False
        return True
    
    def traverse(self, node):
        if (node == None):
            return []
        result = self.traverse(node.left)
        if (len(result) > 0 and result[-1] >= node.val):
            raise Exception()
        result.append(node.val)
        result_right = self.traverse(node.right)
        if (len(result_right) > 0 and result_right[0] <= node.val):
            raise Exception()
        result += result_right
        return result

def make_tree_node(list, node):
    if not node:
        node = TreeNode(list[0])
        del list[0]
        if (len(list) > 0):
            if list[0] != None:
                left = TreeNode(list[0])  
                node.left = left
            del list[0]
        if (len(list) > 0):
            if list[0] != None:
                right = TreeNode(list[0])  
                node.right = right
            del list[0]
    else:
        if (len(list) > 0):
            if list[0] != None:
                left = TreeNode(list[0])  
                node.left = left
            del list[0]
        if (len(list) > 0):
            if list[0] != None:
                right = TreeNode(list[0])  
                node.right = right
            del list[0]
    if (len(list) > 0) and (node.left != None):
        make_tree_node(list, node.left)
    if (len(list) > 0) and (node.right != None):
        make_tree_node(list, node.right)
    return node 

root = make_tree_node([5,1,4,None,None,3,6], None)
print(vars(root))
solution = Solution()
print(solution.isValidBST(root))

root = make_tree_node([2, 2, 2], None)
print(solution.isValidBST(root))

root = make_tree_node([5,4,6,None,None,3,7], None)
print(solution.isValidBST(root))