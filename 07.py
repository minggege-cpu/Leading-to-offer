"""
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
"""


class Solution:
    def __init__(self):
        self.arrList = []

    # 返回对应char
    def FirstAppearingOnce(self):
        return ''.join(self.arrList)

    def Insert(self, char):
        l = []
        count = 0
        for i in char:
            l.append(i)
        for i in range(len(l)):
            if l[i] in l[:i] or l[i] in l[i+1:]:
                continue
            else:
                self.arrList.append(l[i])
                count += 1
                return
        if count == 0:
            self.arrList.append("#")
