import sys
from functools import lru_cache

def maxProfit(prices):
    n = len(prices)
    @lru_cache(typed=True)
    def dfs(i:int, hold:bool) -> int:
        if i < 0:
            return -float('inf') if hold else 0
            # return 'inf' if hold else 0
        if hold:
            return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])
        else:
            return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])
    return dfs(n -1, False)

if __name__ == '__main__':

    prices = input().strip().split()
    # prices = sys.stdin.readline().strip().split()  # 和用input一样，不推荐
    prices = list(map(int, prices))
    
    result = maxProfit(prices)
    print(result)
