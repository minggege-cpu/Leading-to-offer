class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        global count
        global res
        if pRoot is None:
            return
        if count == 1:
            res += [pRoot.val]
        count += 1


res = []
count = 1
