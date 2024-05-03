#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
# 暴力解法，遍历数组中的所有值
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for i in range(0, n):
            if nums[i] == target:
                return i
        return -1 
# 二分查找法
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
# @lc code=end

