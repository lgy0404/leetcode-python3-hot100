from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [] # 存储最终的结果列表
        path = [] # 存储当前的路径列表
        n = len(nums)

        def dfs(i):
            if i == n: # 如果遍历到列表末尾
                ans.append(path.copy()) # 将当前路径加入到结果列表（此时为一个子集）
                return # 结束当前递归

            # 不选 num[i] 的情况
            dfs(i + 1) 

            # 选nums[i]的情况
            path.append(nums[i])# 当前数字加入路径
            dfs(i + 1) # 继续向下遍历
            path.pop() # 回溯，将当前数字移除路径，恢复现场
        dfs(0)
        return ans
if __name__ == '__main__':
    num = input("input:").strip().split()
    num = list(map(int, num))
    solution = Solution()
    ans = solution.subsets(num)
    print(f"ans:{ans}")