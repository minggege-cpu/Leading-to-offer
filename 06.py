"""
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
"""


class Solution1:

    def movingCount(self, threshold, rows, cols):
        self.move(0, 0, threshold, rows, cols)
        # global result
        return len(result)

    def move(self, x, y, threshold, rows, cols):
        global result
        if (x, y) in result:
            return
        if not (0 <= x < rows and 0 <= y < cols): return
        if not self.conflict(x, y, threshold):
            result[(x, y)] = 1
            self.move(x-1, y, threshold, rows, cols)
            self.move(x+1, y, threshold, rows, cols)
            self.move(x, y-1, threshold, rows, cols)
            self.move(x, y+1, threshold, rows, cols)

    def conflict(self, x, y, threshold):
        sums = sum(map(int, str(x) + str(y)))
        return not (sums <= threshold)


result = {}
s = Solution1()
print(s.movingCount(15, 20, 20))



class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        board = [[0 for _ in range(cols)] for _ in range(rows)]

        def block(r,c):
            s = sum(map(int,str(r)+str(c)))
            return s>threshold
        class Context:
            acc = 0
        def traverse(r,c):
            if not (0<=r<rows and 0<=c<cols): return
            if board[r][c]!=0: return
            if board[r][c]==-1 or block(r,c):
                board[r][c]=-1
                return
            board[r][c] = 1
            Context.acc+=1
            traverse(r+1,c)
            traverse(r-1,c)
            traverse(r,c+1)
            traverse(r,c-1)
        traverse(0,0)
        return Context.acc


s = Solution()
print(s.movingCount(15, 20, 20))
