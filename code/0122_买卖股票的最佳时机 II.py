import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        # 定义一个内部函数，用于递归计算最大利润
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int, hold: bool) -> int:
            # 如果当前天数小于0，表示已经遍历完了所有的价格
            if i < 0:
                # 如果持有股票，则无法卖出，返回负无穷
                # 如果不持有股票，则利润为0
                return -inf if hold else 0
            
            # 如果持有股票，可以选择继续持有或者卖出
            if hold:
                # 计算继续持有和卖出后的利润，取其中较大的那个
                return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])
            # 如果不持有股票，可以选择继续不持有或者买入
            else:
                # 计算继续不持有和买入后的利润，取其中较大的那个
                return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])
        
        # 返回在最后一天不持有股票时的最大利润，即整个时间段内的最大利润
        return dfs(n - 1, False)
