from typing import List

# # 下面这个是GPT写的，晦涩难懂！
# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         # 把问题转换为相邻字符中的逗号选还是不选的问题
#         # 从答案的角度
#         ans = []  # 用来存储所有的分割方案
#         path = []  # 用来存储当前的分割方案
#         n = len(s)  # 获取字符串s的长度

#         # 定义dfs函数，i表示当前处理到s的第i个字符，start表示当前分割的起点
#         def dfs(i, start):
#             # 如果 i 等于字符串的长度，说明已经处理完毕
#             if i == n: 
#                 ans.append(path.copy())  # 当前的分割方案复制到ans中
#             else:
#                 for j in range(i, n):
#                     t = s[start: j + 1]  # 获取start到j的子字符串
#                     if t == t[::-1]:  # 判断这个字符串是否是回文
#                         path.append(t)
#                         dfs(j + 1, j + 1)
#                         path.pop()

#         dfs(0, 0)
#         return ans
    
# 下面这个是灵神的解法
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        n = len(s)

        # start 表示当前这段回文子串的开始位置
        def dfs(i: int, start: int) -> None:
            if i == n:
                ans.append(path.copy())  # 复制 path
            else:
                # 不选 i 和 i+1 之间的逗号（i=n-1 时一定要选）
                if i < n - 1:
                    dfs(i + 1, start)

                # 选 i 和 i+1 之间的逗号（把 s[i] 作为子串的最后一个字符）
                t = s[start: i + 1]
                if t == t[::-1]:  # 判断是否回文
                    path.append(t)
                    dfs(i + 1, i + 1)  # 下一个子串从 i+1 开始
                    path.pop()  # 恢复现场

        dfs(0, 0)
        return ans

if __name__ == '__main__':
    res = input("input:").strip()
    solution = Solution()
    res = solution.partition(res)
    print(f"res:{res}")
