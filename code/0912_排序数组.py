import random
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(arr, low, high):
            pivot = arr[low]                                        # 选取最左边为pivot

            left, right = low, high     # 双指针
            while left < right:
                while left<right and arr[right] >= pivot:          # 找到右边第一个<pivot的元素
                    right -= 1
                arr[left] = arr[right]                             # 并将其移动到left处

                while left<right and arr[left] <= pivot:           # 找到左边第一个>pivot的元素
                    left += 1
                arr[right] = arr[left]                             # 并将其移动到right处

            arr[left] = pivot           # pivot放置到中间left=right处
            return left

        def randomPartition(arr, low, high):
            pivot_idx = random.randint(low, high)                   # 随机选择pivot
            arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]     # pivot放置到最左边
            return partition(arr, low, high)                        # 调用partition函数

        def quickSort(arr, low, high):
            if low >= high:             # 递归结束
                return  
            # mid = partition(arr, low, high)       # 以mid为分割点【非随机选择pivot】
            mid = randomPartition(arr, low, high)   # 以mid为分割点【随机选择pivot】
            quickSort(arr, low, mid-1)              # 递归对mid两侧元素进行排序
            quickSort(arr, mid+1, high)

        quickSort(nums, 0, len(nums)-1)             # 调用快排函数对nums进行排序
        return nums

if __name__ == '__main__':
    arr = input("Enter space-separated integers: ").strip().split() # strip() 函数在 Python 中可以用于移除字符串首尾的特定字符。
    arr = list(map(int, arr))  # map() 函数是 Python 中的一个内置函数，它接受两个参数：一个函数和一个可迭代对象。它的作用是将传入的函数应用到可迭代对象的每个元素上，并返回一个新的迭代器。list() 函数用于将一个迭代器或其他可迭代对象转换成一个列表。
    solution = Solution() # 实例化类
    sortarr = solution.sortArray(arr) # 调用类中的方法函数
    print(sortarr)
