# leetcode习题解答

这里会有我刷leetcode的习题解答，很多都是看讨论区学到的，然后自己重写了一遍。

## 目录

* [1. Two Sum](#1-two-sum)
* [9. Palindrome Number](#9-palindrome-number)
* [15. 3Sum](#15-3sum)
* [17. Letter Combinations of a Phone Number](#17-letter-combinations-of-a-phone-number)
* [23. Merge k Sorted Lists](#23-merge-k-sorted-lists)
* [24. Swap Nodes in Pairs](#24-swap-nodes-in-pairs)
* [26. Remove Duplicates from Sorted Array](#26-remove-duplicates-from-sorted-array)
* [29. Divide Two Integers](#29-divide-two-integers)
* [30. Substring with Concatenation of All Words](#30-substring-with-concatenation-of-all-words)
* [31. Next Permutation](#31-next-permutation)
* [54. Spiral Matrix](#54-spiral-matrix)
* [66. Plus One](#66-plus-one)

## 1. Two Sum

注意返回的是位置：

python的小trick，**enumerate()**，把数组变成字典。

首先，如果有一个字典dict{}，其key为nums[i]，value为i。我们只需要便利nums，求difference = target - nums[i]。判断dict[difference]是否在dict{nums[i]}和difference[difference]中即可。

```python
dic = dict()
# 使用enumerate遍历nums[]
for index, value in enumerate(nums):
    # 求差
    difference = target - value
    # 判断差是否在dict里面，dict是使用key判断的。
    if difference in dic:
        '''
        如果difference在里面
        difference就是之前遍历过的，
        被存储到dict中,dic[difference]
        就是difference在数组中的位置，
        index就是此时被剪去的value的位置。
        '''
        return [dic[difference], index]
    else:
        # 将上面不在dict中的数存进去，注意这里的key是数组中数字的值，value数字位置
        dic[value] = index
```

## 9. Palindrome Number

一行代码就OK了，str(x)把x转字符串倒序后和str(x)比一下就OK。

```python
return str(x)[::-1] == str(x)
```

## 15. 3Sum

>

```python

"""
:type nums: List[int]
:rtype: List[List[int]]
"""
if len(nums) < 3:
    return []
nums.sort()
res = set()
# 先循环从 nums[:-2]中找出一个v
for i, v in enumerate(nums[:-2]):
    # 因为已经排序过，所以v和前一个数一样的话 情况一样 直接continue
    if i >= 1 and v == nums[i-1]:
        continue
    d = {}
    # 从nums[i+1:]中找一个x
    # 当第一个数v确定时，我们需要的就是在nums[i+1:]中找出两个数相加等于v
    for x in nums[i+1:]:
        # 如果这个x不在d中我们就先把-v-x添加进去 -v-x代表我们要找的第三个数
        # -v-x实质代表这个问题被化成了2sum
        if x not in d:
            d[-v-x] = 1
        else:
            res.add((v, -v-x, x))
            gen = map(list, res)
            arry = list()
            for g in gen:
                arry.append(g)
```

## 17. Letter Combinations of a Phone Number

1. 首先可以考虑用一个字典将数字和单词对应起来
2. 在循环里面便利digits。
3. 当遍历第一个的时候，将第一个数字对应的字母，添加到out中。

```python
k = [j+i for i in self.num_value[digit] for j in out]

#看上去很复杂，其实就是以下代码的简化

for j in out:
    for i in self.num_value[digit]:
        k.append(j+i)
```

## 23. Merge k Sorted Lists

用一个最笨的方法就可以了，把所有元素添加到一个list中，list排序后，再用这个list生成一个链表。

## 24. Swap Nodes in Pairs

使用递归解决这题。
递归的主体就是我递归1、3、5...这些节点。
然后:

```python
1.next = recursion(3)
# 1节点的下一个是递归返回的list
2.next = 1
# 完成交换1 2的交换

temp = head.next
head.next, temp.next = self.swapPairs(temp.next), head
return temp

```

递归的出口就是1 2 为空，

```python
if head and head.next:
    recursion
```

当head和head.next为空时：

```python
    return head
```

其实就是返回空

## 26. Remove Duplicates from Sorted Array

```python
from collections import OrderedDict
# 导入OrderedDict
return len(OrderedDict.fromkeys(nums))
```

OrderedDict.fromkeys(nums)使用nums中的值作为key。

## 29. Divide Two Integers

最简单的办法就是用减法替代除法，但是时间会超。
所以用一个很有意思的方法去做。

```python
while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp
            res += i
            i <<= 1
            temp <<= 1
```

这里有两个while,temp用来替代divisor，也是由于temp, i我们可以快速的迭代。
先说内层的while，内层的while执行第一次循环后，res += i，i和temp都变为原来两倍，
如果继续满足内层while循环，那么res就会加两倍i，temp和继续变大。
如果不满足内层while，说明由于temp和i增长太大，dividend减不起temp了，但是也许可以能减的起divisor。
所以我们再次循环这个temp和i变大的过程，当dicidend连divisor都减不起的时候，就退出了。

> 1.我先减去divisior，再减2倍的divisor，再减4倍的。
> 2.当dividend减不起时，再次执行第1步

当减到dividend - divisor减不起时，退出。

## 30. Substring with Concatenation of All Words

题目就是从s中找出一个子串，子串中包含所有的words中的词。

思路：
> 因为要包含所有的词，所以我们是知道s的子串的长度的。所以我们可以不断取出字串。其实就是滑窗法。
> 因为每个词语的长度相同，所以我们是可以把子串中的单词提取出来。
> 我们只要判断子串中的单词是否和words中的一样即可。

window_length表示字串长度。word_window表示子串。temp是把字串按词分开，存入temp中。
判断temp是否和words相同即可。

Counter()会返回一个字典，其key为list中的单词，value是单词出现的次数。

## 31. Next Permutation

全排列，就是说下一个是能找到的最小的大于上一个数。
这一题分为两步：

1. 从右往左找到第一个不递增的元素i。（1，4，2）就是找到4
2. 从右往左找到第一个大于i-1的元素j，并将其交换位置。
3. 将i和后面的元素[i,end]不断交换首尾。

## 54. Spiral Matrix

矩阵转换，可以通过行列变换和行倒(matrix[::-1])实现。
顺时针转换:先行倒过来，再zip

```python
matrix = matrix[::-1]
matrix = list(list(i) for i in zip(*matrix))

## 合起来就是
matrix = list(list(i) for in zip(*matrix[::-1]))
```

逆时针转换:先zip,再行倒过来

```python
matrix = list(list(i) for i in zip(*matrix))
matrix = matrix = matrix[::-1]

## 合起来就是
matrix = list(list(i) for i in zip(*matrix))[::-1]
```

这一题的写法就是 先pop第一行，再逆时针旋转矩阵，再pop第一行，不断重复直到矩阵中没有数。

```python
while matrix:
    res = res + matrix.pop(0)
    matrix = list(list(i) for i in zip(*matrix))[::-1]
```

这一题的思路对59题也有帮助，这里是pop，59题是生成。

## 66. Plus One

两种方法
第一种:
最传统的，倒序遍历nums，
如果nums[i] 小于9，直接nums[i] + 1 再return就OK，
等于9时，nums[i] = 0,再看nums[i-1]是否小于9，逻辑同上。
如果遍历完数组后，还没有return，说明这个数组里面全是9，直接return [1]+[0]*len(nums)

```python
for i in range(len(digits)):
    if digits[~i] < 9:
        digits[~i] += 1
        return digits
    digits[~i] = 0
return [1] + [0] * len(digits)
```

~i 是按位取反操作，通过取反我们就能得到倒数第i+1个数。
例如i = 0时，\~i是-1 所以使用\~i就可以实现倒序查看nums了。

第二种：
把list转换成str，再变成int，+1之后，再转成str，然后一个转int存入到list中。

```python
result = []
for i in str(int(''.join(str(i) for i in digits)) + 1):
    result.append(int(i))
```
