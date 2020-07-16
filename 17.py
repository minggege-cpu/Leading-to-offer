"""
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if k == 0:
            return None
        if not pRoot:
            return None
        deque = [pRoot]
        res = []
        while deque:
            cur_node = deque.pop(0)
            res.append(cur_node.val)
            if cur_node.left:
                deque.append(cur_node.left)
            if cur_node.right:
                deque.append(cur_node.right)
        res.sort()
        return res[k-1]


t1 = TreeNode(5)
t2 = TreeNode(3)
t3 = TreeNode(7)
t4 = TreeNode(2)
t5 = TreeNode(4)
t6 = TreeNode(6)
t7 = TreeNode(8)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7
s = Solution()
print(s.KthNode(t1, 1))