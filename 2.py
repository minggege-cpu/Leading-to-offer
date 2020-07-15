"""
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
用例:
[5,2,3,4,1,6,7,0,8]

对应输出应该为:

"5.00 3.50 3.00 3.50 3.00 3.50 4.00 3.50 4.00 "
"""


from heapq import *


class Solution(object):
    def __init__(self, ):
        self.numList = []

    def Insert(self, num):
        self.numList.append(num)

    def GetMedian(self, s):
        self.numList.sort()
        n = len(self.numList)
        if n % 2 == 1:
            return self.heap[n // 2]
        else:
            return (self.heap[n // 2] + self.heap[n // 2 - 1]) / float(2)


if __name__ == "__main__":
    l = [5, 2, 3, 4, 1, 6, 7, 0, 8]
    s = Solution()
    for i in l:
        s.Insert(i)
        print(s.GetMedian(1))