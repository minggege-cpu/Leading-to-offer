"""
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
"""

# class Solution:
#     # s, pattern都是字符串
#     def __init__(self):
#         self.s = []
#
#     def match(self, s, pattern):
#         self.s.append(s)
#         a = ['.', '*']
#         if len(s) == 0 and len(pattern) == 0:
#             return True
#         elif len(s) == 0 and pattern == '.':
#             return False
#         elif len(s) == 0 and pattern[-1] == '*':
#             return True
#         elif len(s) == 0 and len(pattern) != 0 or len(s) != 0 and len(pattern) == 0:
#             return False
#         for i in range(len(pattern)):
#             if pattern[i] not in a and pattern[i] == s[i]:
#                 return self.match(s[i+1:], pattern[i+1:])
#             elif pattern[i] not in a and pattern[i] != s[i]:
#                 return False
#             if pattern[i] == '.':
#                 return self.match(s[i+1:], pattern[i+1:])
#             if pattern[i] == '*':
#                 has1 = self.match(s[i+1:], pattern[i + 1:])
#                 has2 = self.match(self.s[0], pattern[i + 1:])
#                 return has1 or has2


class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if s == pattern:
            return True
        if len(pattern)>1 and pattern[1] == '*':
            if s and (s[0]==pattern[0] or pattern[0] == '.'):
                return self.match(s,pattern[2:]) or self.match(s[1:],pattern)
            else:
                return self.match(s,pattern[2:])
        elif s and pattern and (s[0] == pattern[0] or pattern[0]=='.'):
            return self.match(s[1:],pattern[1:])
        return False


s = Solution()
print(s.match('aaa', 'abb*ac*a'))