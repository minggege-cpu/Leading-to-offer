"""
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
（注意：规定B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2];）
即不包含以自身下标相同元素的乘积
"""


class Solution:
    def multiply(self, A):
        B = []
        for i in range(len(A)):
            sums = 1
            for j in range(len(A)):
                if i == j:
                    continue
                sums *= A[j]
            B.append(sums)
        return B


s = Solution()
print(s.multiply([1, 2, 3, 4, 5, 123, 15, 0]))
