# -*- coding: utf-8 -*-

"""
414. 第三大的数

给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

输入: [2, 2, 3, 1]
输出: 1

解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
存在两个值为2的数，它们都排第二。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/third-maximum-number
"""

class Solution:
    def thirdMaxSort(self, nums: list) -> int:
        """
        这个好像不算O(n) sort()是O(nlogn)
        """
        if not nums:
            return None
        nums = list(set(nums))
        nums.sort(reverse=True)
        if len(nums) < 3:
            return nums[0]
        return nums[2]

    def thirdMax(self, nums: list) -> int:
        nums = list(set(nums))
        max_time = 3
        if len(nums) < 3:
            max_time = 1
        while max_time:
            num_max = False
            for num in nums:
                if not num_max or num > num_max:
                    num_max = num
            max_time -= 1
            nums.remove(num_max)
        return num_max


if __name__ == "__main__":
    print(Solution().thirdMax([2, 2, 3, 1]))