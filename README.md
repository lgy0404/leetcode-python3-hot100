# 【leetcode】刷题记录 python实现 🔥hot100+简单题顺序做

​	备注：

- 每个题解包含含题目、解题思路、python3程序、问题思考与解答
- 🟢表示”简单题“，🟡表示”中等题“，🔴表示”困难题“

## 🆕最新消息

- 2023年8月16日：上传了前6题的题解
- 2023年8月17日：
	- 上传了**0042接雨水**的题解
	- 笔记目录改为列表的形式
	- 题目命名空格改为下划线
	- 增加题目难易度
	- 找到了一个很棒的力扣刷题插件[labuladong 的算法小抄 | labuladong 的算法小抄](https://labuladong.github.io/algo/)
- 2023年8月22日：
	- 复习**0042接雨水**的题解
	- 之后的题解主要参考算法小抄中的思想进行重述，加深印象
	- 做了美团20数据岗笔试题**寻找最高的山峰**
	- 滑动窗口开篇，晚上看了算法小抄
- 2023年8月23日：
	- 做了滑动窗口**0003最长无重复字串**
	- 更新了题解但是没怎看懂
	- 体会：以后每天先一个简单题+一个hot100，要不要没自信了QAQ
- 2023年8月24日：
  - 早上研读了算法小抄中关于滑动窗口的解说
  - 更新了**0009回文数**的题解
  - 调整项目目录格式
  - 新增 *收获* 栏
  - 更新了**0438_找到字符串中所有字母异位词**的题解
- 2023年8月29日：
	- 更新了**0013_罗马数字转整数**的题解
	- **总结了滑动窗口解题模板，还需进一步理解**

- 2023年8月30日：
	- 更新了**0014_最长公共前缀**的题解
	- 更新了**0560_和为K的子数组**的题解

- 2023年8月30日：

	- 更新了**0020_有效的括号**的题解

	- **滑动窗口最大值问题没有搞明白**
	
	- **计划总结括号相关问题的题解**

### hot100刷题记录

| hot100序 | 题解链接                                                     | 解法                                 | 考察知识 | 难度 | 总序 | 收获                                                     |
| :------: | :----------------------------------------------------------- | :----------------------------------- | :------: | :--: | :--: | -------------------------------------------------------- |
|    01    | [两数之和](./hot100/01_哈希_简单_0001_两数之和_230727.md)    | 1.暴力循环<br/>2.哈希表              |   哈希   |  🟢   | 0001 |                                                          |
|    02    | [字母异位词分组](./hot100/02_哈希_中等_0049_字母异位词分组_230802.md) | 1.排序<br/>2.计数                    |   哈希   |  🟡   | 0049 |                                                          |
|    03    | [最长连续序列](./hot100/03_哈希_中等_0128_最长连续序列_230809.md) | 1.哈希表                             |   哈希   |  🟡   | 0128 |                                                          |
|    04    | [移动零](./hot100/04_指针_简单_0283_移动零_230814.md)        | 1.冒泡排序(超时)<br/>2.快慢指针      |   指针   |  🟢   | 0283 |                                                          |
|    05    | [盛水最多的容器](./hot100/05_指针_中等_0011_盛最多水的容器_230816.md) | 1.对撞指针<br/>2.暴力循环(超时)      |   指针   |  🟡   | 0011 |                                                          |
|    06    | [三数之和](./hot100/06_指针_中等_0015_三数之和_230816.md)    | 1.对撞指针                           |   指针   |  🟡   | 0015 |                                                          |
|    07    | [接雨水](./hot100/07_指针_困难_0042_接雨水_230817.md)        | 1.单调栈<br/>2.韦恩图                |   指针   |  🔴   | 0042 |                                                          |
|    08    | [无重复最长字串](./hot100/08_指针_中等_0003_无重复最长字串_230823.md) | 1.哈希表<br>2.滑动窗口<br>3.快慢指针 | 滑动窗口 |  🟡   | 0003 |                                                          |
|    09    | [找到字符串中所有字母异位词](./hot100/09_滑动窗口_中等_0438_找到字符串中所有字母异位词_230824.md) | 1.哈希表<br>2.滑动窗口<br>3.快慢指针 | 滑动窗口 |  🟡   | 0438 | 1.总结滑动窗口解题模板                                   |
|    10    | [和为K的子数组](./hot100/10_子串_中等_0560_和为K的子数组_230830.md) | 1.哈希表<br>2.前缀和<br>             |   字串   |  🟡   | 0560 | 1.定义默认字典a=collections.defaultdict(int)<br>2.前缀和 |



### 每天一个简单题

| 刷题序 | 题解链接                                                     | 解法                                                |       考察知识       | 总序 | 收获                                                         |
| :----: | :----------------------------------------------------------- | :-------------------------------------------------- | :------------------: | :--: | ------------------------------------------------------------ |
|   01   | [回文数](./每天一道简单题/01_数学_简单_0009_回文数_230824.md) | 1.数学运算进行整数反转<br/>2.转回字符串进行切片反转 |         数学         | 0009 | 1.取余`%`<br>2.字符串切片反转s`[::-1]`                       |
|   02   | [罗马数字转整数](./每天一道简单题/02_字符串、指针、哈希表_简单_0013_罗马数字转整数_230829.md) | 1.哈希表存值，指针遍历累加                          | 字符串、指针、哈希表 | 0023 | 1.给定字符串s可以直接取`s[0]`<br>2.字符串切片反转s`[::-1]`   |
|   03   | [最长公共前缀](./每天一道简单题/03_字符数组_简单_0014_最长公共前缀_230830.md) | 1.纵向遍历<br>2.巧用max/min(字符数组)按字典排序     |       字符数组       | 0014 | 1.max/min(字符数组)按字典排序                                |
|   04   | [有效的括号](./每天一道简单题/04_栈_简单_0020_有效的括号_230831.md) | 1.栈<br>                                            |      哈希表、栈      | 0014 | 1.使用栈进行括号关系判断<br>2.使用哈希表记录左右括号的关系<br>3.[总结括号相关的问题的解法](https://labuladong.github.io/algo/di-san-zha-24031/jing-dian--a94a0/ru-he-jie--306f6/) |



## 📒模板总结

### 滑动窗口

参考：[我写了首诗，把滑动窗口算法算法变成了默写题 | labuladong 的算法小抄](https://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-48c1d/wo-xie-le--f7a92/)

#### 相关题目

| LeetCode                                                     | 力扣                                                         | 难度 |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :--: |
| [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) |  🟡   |
| [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | [438. 找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) |  🟡   |
| [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/) | [567. 字符串的排列](https://leetcode.cn/problems/permutation-in-string/) |  🟡   |
| [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | [76. 最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/) |  🔴   |
| -                                                            | [剑指 Offer 48. 最长不含重复字符的子字符串](https://leetcode.cn/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/) |  🟡   |
| -                                                            | [剑指 Offer II 014. 字符串中的变位词](https://leetcode.cn/problems/MPnaiL/) |  🟠   |
| -                                                            | [剑指 Offer II 015. 字符串中的所有变位词](https://leetcode.cn/problems/VabMRr/) |  🟡   |
| -                                                            | [剑指 Offer II 016. 不含重复字符的最长子字符串](https://leetcode.cn/problems/wtcaE1/) |  🟡   |
| -                                                            | [剑指 Offer II 017. 含有所有字符的最短字符串](https://leetcode.cn/problems/M1oyTv/) |  🔴   |

#### 答题模板

这个算法技巧的思路非常简单，就是维护一个窗口，不断滑动，然后更新答案么。LeetCode 上有起码 10 道运用滑动窗口算法的题目，难度都是中等和困难。该算法的大致逻辑如下：

```python
left = 0, right = 0
while left < right && right < len(s):
    # 增大窗口
    
    while window need shrink:
        # 缩小窗口
```

以找到**字符串中的所有字母异位词**为例，详细的答题模板如下：

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 用合适的数据结构记录窗口中的数据，一般是哈希表，此处以哈希表为例
        # 初始化目标字符串与滑动窗口的哈希表，字符做键，字符个数做值
        need, window = defaultdict(int), defaultdict(int)
        # 将给定字符串的属性赋值到已经初始化好的哈希表中
        for c in p:
            need[c] += 1
        # 初始化快慢指针与返回值
        left, right = 0, 0 
        res = []
        '''初始化覆盖程度【本题用】
        valid = 0
        '''

        # 判断是否还需要进行窗口滑动
        while right < len(s):
            c = s[right] # c是要加进窗口的字符
            right += 1 # 扩大窗口
            '''进行窗口内一系列数据的更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            '''
            # 判断左侧窗口是否需要收缩(left < right and window needs shrink(这里是窗口的长度大于给定p的长度))
            while right - left >= len(p):
                '''当串口符合条件时，将起始索引加入res【本题用】
                if valid == len(need):
                    res.append(left)
                '''
                d = s[left] # d是将移出窗口的字符
                left += 1 # 增大左指针进行窗口收缩
                '''进行窗口内一系列数据的更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                window[d] -= 1
                '''
        return res
```

#### 应用示例

##### [438. 找到字符串中所有字母异位词 - 力扣（LeetCode）](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 初始化目标字符串与滑动窗口的哈希表，字符做键，字符个数做值
        need, window = defaultdict(int), defaultdict(int)
        # 将给定字符串的属性赋值到已经初始化好的哈希表中
        for c in p:
            need[c] += 1
        # 初始化快慢指针，覆盖程度与返回值
        left, right = 0, 0 
        valid = 0
        res = []

        # 判断是否还需要进行窗口滑动
        while right < len(s):
            c = s[right] # c是要加进窗口的字符
            right += 1 # 扩大窗口
            # 进行窗口内一系列数据的更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            # 判断左侧窗口是否需要收缩（窗口的长度大于给定p的长度）
            while right - left >= len(p):
                #  当串口符合条件时，将起始索引加入res
                if valid == len(need):
                    res.append(left)
                d = s[left] # d是将移出窗口的字符
                left += 1 # 增大左指针进行窗口收缩
                # 进行窗口内一系列数据的更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                window[d] -= 1

        return res
```

思考：为什么这里不能交换位置？

![image-20230829175714763](https://lgy0404.oss-cn-shanghai.aliyuncs.com/typoraimage-20230829175714763.png)



### 单调队列结构解决滑动窗口问题

参考：[单调队列结构解决滑动窗口问题 | labuladong 的算法小抄](https://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-daeca/dan-diao-d-32cd5/)

#### 应用示例

##### [239. 滑动窗口最大值 - 力扣（LeetCode）](https://leetcode.cn/problems/sliding-window-maximum/description/?envType=study-plan-v2&envId=top-100-liked)
