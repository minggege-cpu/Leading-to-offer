"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
例如
        a  b  c  e
        s  f  c  s
        a  d  e  e
矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""


class Solution:

    def hasPath(self, matrix, rows, cols, path):
        global memo
        chart = [[0 for i in range(cols)]for j in range(rows)]
        for i in range(rows):
            for j in range(cols):
                chart[i][j] = matrix[i*cols+j]
        start_code = path[0]
        for i in range(len(chart)):
            print(chart[i])
        start = []
        for l in range(len(chart)):
            if start_code in chart[l]:
                dic = [(l, i) for i, j in enumerate(chart[l]) if j == start_code]
                start.append(dic)
        if len(start) == 0:
            return False
        has = True
        for s in start:
            for s1 in s:
                memo[(s1[0], s1[1])] = 1
                has = self.findPath(chart, s1[0], s1[1], rows, cols, 1, path)
                if has:
                    return True
                memo = {}
        return has

    def findPath(self, chart, x, y, rows, cols, count, path):
        global memo
        directions = [(1, 0), [-1, 0], [0, 1], [0, -1]]
        nums = count
        if count == len(path):
            return True
        for dir in directions:
            i = x+dir[0]
            j = y+dir[1]
            if i < 0 or j < 0 or i >= rows or j >= cols:
                continue
            if (i, j) in memo:
                continue
            if chart[i][j] == path[count]:
                count += 1
                memo[(i, j)] = 1
                if self.findPath(chart, i, j, rows, cols, count, path):
                    return True
                del memo[(i, j)]
                count = nums

        return False


memo = {}
s = Solution()
print(s.hasPath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS", 5, 8, "SGGFIECVAASABCEHJIGQEMS"))
