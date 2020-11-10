'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2018-12-17 21:19:33
@LastEditors: jxxiao
@LastEditTime: 2020-04-07 17:04:36
'''
# 模拟手写的过程，创建一个numrow个字符串的数组，每次写完第一个和最后一个就变方向。最后得到三个字符串。


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        i, direction = 0, -1
        arr = [''] * numRows
        for char in s:
            arr[i] += char
            if i == 0 or i == numRows - 1:
                direction *= -1
            i += direction
        return "".join(arr)

Solution().convert('leetcode', 3)