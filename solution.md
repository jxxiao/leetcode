[TOC]

# 1.Two Sum

注意返回的是位置：

python的小Trick，**enumerate()**，把数组变成字典。

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
       	如果difference在里面，difference就是之前遍历过的，
       	被存储到dict中,dic[difference]就是difference在数组中的位置，
       	index就是此时被剪去的value的位置。
        '''
        return [dic[difference], index]
    else:
        # 将上面不在dict中的数存进去，注意这里的key是数组中数字的值，value数字位置
        dic[value] = index
```

# 15. 3Sum

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

# 17. Letter Combinations of a Phone Number

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

# 24.Swap Nodes in Pairs

使用递归解决这题。
递归的主体就是我递归1、3、5...这些节点。
然后:

```python
1.next = recursion(3)
# 1节点的下一个是递归返回的list
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