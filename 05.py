# class Solution(object):
#     def intersect(self, nums1, nums2):
#         res = []
#         for i in nums1:
#             if i in nums2:
#                 res.append(i)
#                 nums2.remove(i)
#         return res
#
#
# s = Solution()
# print(s.intersect([1, 2, 2, 1], [2, 2]))


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None


s = Solution()
print(s.twoSum([1, 2, 2, 1], 3))
