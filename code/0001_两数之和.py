#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #哈希表解题
        hashtable = {}
        for index,val in enumerate(nums):
            if target - val not in hashtable:
                hashtable[val] = index
            else:
                return [hashtable[target - val],index]
# @lc code=end

