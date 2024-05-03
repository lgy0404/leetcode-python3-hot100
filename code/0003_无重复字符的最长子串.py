#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}

        left = right = 0
        res = 0 # 记录结果
        while right < len(s):
            c = s[right]
            right += 1
            # 进行窗口内数据的一系列更新
            window[c] = window.get(c, 0) + 1
            # 判断左侧窗口是否要收缩
            while window[c] > 1:
                d = s[left]
                left += 1
                # 进行窗口内数据的一系列更新
                window[d] -= 1
            # 在这里更新答案
            res = max(res, right - left)
        return res
# @lc code=end

