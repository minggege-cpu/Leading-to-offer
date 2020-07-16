"""
首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。
每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,
从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。
请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)
"""


class Solution:
    def LastRemaining_Solution(self, n, m):
        if n <= 0:
            return -1
        if m == n == 1:
            return 0
        l = [i for i in range(n)]
        i = 0
        while len(l) != 1:
            i = (m+i-1) % len(l)
            l.pop(i)
        return l[0]


s = Solution()
print(s.LastRemaining_Solution(5, 3))