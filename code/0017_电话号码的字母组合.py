from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 注意这个题目好像不一定是子集型回溯
        # 定义一个字符串数组用于存储电话号码的对应关系, 这样比直接定义哈希表要简单
        MAPPING = [" ", " ", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        # 处理特殊情况-给定的电话号码为空
        n = len(digits)
        if n == 0:
            return []
        # 使用一个path记录已经走过的路径，思考这里path的数据格式是怎么确定的？根据要求的返回值的格式，其实最后这道题中返回值就是搜索树的叶子节点（字符串）组成的字符串数组
        path = [""] * n
        # 初始化答案返回值
        ans = []
        # 定义dfs，实现深度优先搜索，dfs(i)表示构造>= i的字母组合
        def dfs(i):
            if i == n: # 如果i = n代表找到了一种解决方案
                ans.append("".join(path))   # 为数组添加元素使用append，最后这一步其实要实现的的是，把path copy给ans？ 见解析
                return
            for x in MAPPING[int(digits[i])]:
                path[i] = x # path里边存的到底是啥啊！
                dfs(i + 1)
        dfs(0)
        return ans

if __name__ == '__main__':
    # 输入电话号码
    num = input("input:").strip().split()
    # 转换为数组
    num = list(map(int, num))
    # 实例化类
    solution = Solution()
    # 调用类中的方法
    ans = solution.letterCombinations(num)
    print(f"ans:{ans}")