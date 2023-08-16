# 【🔥leetcode hot100 】题解 python实现

备注：每个题解包含含题目、解题思路、python3程序、问题思考与解答

## 🆕最新消息

- 2023年8月16日：上传了前5题的题解

## 📔笔记目录

[01 leetcode 哈希 0001 两数之和 230727](./01%20leetcode%20哈希%200001%20两数之和%20230727.md)

[02 leetcode 哈希 0049 字母异位词分组 230802](./02%20leetcode%20哈希%200049%20字母异位词分组%20230802.md)

[03 leetcode 哈希 0128 最长连续序列 230809](./03%20leetcode%20哈希%200128%20最长连续序列%20230809.md)

[04 leetcode 指针 283 移动零 230814](./04%20leetcode%20指针%20283%20移动零%20230814.md)

[05 leetcode 指针 0011 盛最多水的容器 230816](./05%20leetcode%20指针%200011%20盛最多水的容器%20230816.md)



## 一个示例

**03 leetcode 哈希 0128 最长连续序列 230809**

# [0128. 最长连续序列](https://leetcode.cn/problems/longest-consecutive-sequence/)

- 标签：并查集、数组、哈希表
- 难度：中等

## 题目大意

**描述**：给定一个未排序的整数数组 `nums`。

**要求**：找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。并且要用时间复杂度为 $O(n)$ 的算法解决此问题。

**说明**：

- $0 \le nums.length \le 10^5$。
- $-10^9 \le nums[i] \le 10^9$。

**示例**：

- 示例 1：

```Python
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
```

- 示例 2：

```Python
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
```

# 二、我的题解

## **哈希表**

题目要求 $O(n)$ 复杂度。

- 用哈希表存储`每个端点值对应连续区间的长度`
- 若数已在哈希表中：
	- 跳过不做处理
- 若是新数加入：
	- 取出其左右相邻数已有的连续区间长度 left 和 right
	- 计算当前数的区间长度为：cur_length = left + right + 1
	- 根据 cur_length 更新最大长度 max_length 的值
	- 更新区间两端点的长度值

| 哈希表的键         | 哈希表的值                   |
| ------------------ | ---------------------------- |
| 给定的数组中的元素 | 每个端点值对应连续区间的长度 |



### **python3程序**


```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_dict = dict()

        max_length = 0
        for num in nums:
            if num not in hash_dict:
                left = hash_dict.get(num - 1, 0)
                right = hash_dict.get(num + 1, 0 )

                cur_length = 1 + left + right
                if cur_length > max_length:
                    max_length = cur_length

                hash_dict[num] = cur_length
                hash_dict[num - left] = cur_length
                hash_dict[num + right] = cur_length

        return max_length
```

- `具体实现`

1. 定义一个名为 `Solution` 的类，它包含一个名为 `longestConsecutive` 的方法，该方法接受一个参数 `nums`，该参数是一个整数列表，并返回一个整数作为结果。

2. 创建一个空的字典 `hash_dict`，用于存储每个数字及其对应的连续序列长度。

3. 初始化一个变量 `max_length`，用于记录最长连续序列的长度。

4. 遍历输入的整数列表 `nums`，对于列表中的每个数字 `num`，执行以下操作：

	a. 检查当前数字 `num` 是否已经在 `hash_dict` 中，如果不在，则进行以下操作：

	b. 从 `hash_dict` 中获取数字 `num - 1` 对应的连续序列长度，如果不存在则默认为 0，赋值给变量 `left`。

	c. 从 `hash_dict` 中获取数字 `num + 1` 对应的连续序列长度，如果不存在则默认为 0，赋值给变量 `right`。

	d. 计算当前数字 `num` 所在连续序列的长度 `cur_length`，它等于 1 加上 `left` 和 `right` 的值。即当前数字连续序列的长度等于左侧连续序列长度、当前数字、右侧连续序列长度的总和。

	e. 如果当前连续序列长度 `cur_length` 大于 `max_length`，则更新 `max_length` 为 `cur_length`，以记录当前找到的最长连续序列。

	f. 在 `hash_dict` 中更新数字 `num` 对应的连续序列长度为 `cur_length`。

	g. 更新 `hash_dict` 中的键值对，将数字 `num - left` 的连续序列长度更新为 `cur_length`，将数字 `num + right` 的连续序列长度更新为 `cur_length`。这是因为当前数字的存在可能延伸并连接之前的连续序列，所以需要更新左右两侧数字的连续序列长度。

5. 遍历完成后，返回变量 `max_length`，即找到的最长连续序列长度。

- `总结`

	在遍历数组时，使用了哈希表 `hash_dict` 来存储每个数字的连续序列长度信息，这样可以在 $O(1)$ 的时间内**检查某个数字的连续序列长度**，从而在线性时间内完成整个数组的遍历和序列长度计算。同时，通过动态更新左右相邻数字的连续序列长度，确保了最终得到的连续序列长度是准确的。

### **复杂度分析**

- **时间**复杂度：**$O(n)$**
- **空间**复杂度：待考证

![image-20230809194544359](https://lgy0404.oss-cn-shanghai.aliyuncs.com/typoratyporaimage-20230809194544359.png)

### **思考与收获**

#### `if num not in hash_dict` 这里说的`num`是`hash_dict`的键还是值？

`num` 是指作为字典 `hash_dict` 的键。这行代码 `if num not in hash_dict:` 检查当前数字 `num` 是否已经存在于字典 `hash_dict` 的键中。如果 `num` 不在字典的键中，就意味着这个数字尚未被处理过，需要进行后续的计算和更新操作。

#### 详细解释 left = hash_dict.get(num - 1, 0)，尤其是hash_dict.get的用法？

首先需要理解字典（Python 中的 `dict`）的 `.get()` 方法的用法。`.get()` 方法用于从字典中获取指定键的值，如果键不存在，则返回一个默认值。具体来说：

- 如果键存在于字典中，`.get()` 方法返回对应的值。
- 如果键不存在于字典中，`.get()` 方法返回提供的默认值。

在这个程序中，`hash_dict` 是一个字典，用于存储数字及其对应的连续序列长度。在连续序列计算的过程中，为了确定当前数字 `num` 所在的连续序列长度，需要查找数字 `num - 1` 在字典中对应的连续序列长度。

解释 `left = hash_dict.get(num - 1, 0)` 这行代码：

1. `num - 1` 是要查找的键，即用于确定当前数字 `num` 左侧的数字。
2. `hash_dict.get(num - 1, 0)` 意味着从 `hash_dict` 字典中获取键为 `num - 1` 的值，如果键不存在，则返回默认值 `0`。

这个操作的目的是检查在 `hash_dict` 中是否有关于数字 `num - 1` 的连续序列长度信息。如果存在，那么 `left` 将被赋值为 `num - 1` 对应的连续序列长度，否则 `left` 将被赋值为 `0`，这是因为在连续序列的计算中，如果左侧的数字不存在，则默认为 `0`。

总之，`hash_dict.get(num - 1, 0)` 这个操作是为了获取数字 `num - 1` 在 `hash_dict` 中的连续序列长度（如果存在），或者返回默认值 `0`（如果不存在）。这个信息将用于计算当前数字 `num` 所在连续序列的长度。

 参考：[128. 最长连续序列 - 力扣（LeetCode）https://leetcode.cn/problems/longest-consecutive-sequence/solutions/3956/dong-tai-gui-hua-python-ti-jie-by-jalan/?envType=study-plan-v2&envId=top-100-liked)
