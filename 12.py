"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c
所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
即给定一个字符串
求改字符串的全排列
"""


# import itertools
# class Solution:
#     def Permutation(self, ss):
#         if not ss:
#             return ss
#         result = map(lambda x: ''.join(x), itertools.permutations(ss))
#         result = list(set(result))
#         result.sort()
#         return result


class Solution:
    def Permutation(self, ss):
        if len(ss) <= 1:
            return ss
        res = set()
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i]+ss[i+1:]):
                res.add(ss[i]+j)
        return sorted(res)


s = Solution()
print(s.Permutation("ABCD"))

