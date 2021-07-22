# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:                
                
        def dfs(node, parent):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)
                
        dfs(root, None)
        answer = []
        look = set()
        queue = collections.deque()
        queue.append([target,0])
        while queue:
            node, distance = queue.pop()
            if distance == k:
                answer.append(node.val)
            look.add(node)
            if node.left and not node.left in look:
                queue.append([node.left, distance+1])
            if node.right and not node.right in look:
                queue.append([node.right, distance+1])
            if node.parent and not node.parent in look:
                queue.append([node.parent, distance+1])
            
        return answer