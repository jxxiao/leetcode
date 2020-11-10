'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2018-12-17 21:19:33
@LastEditors: jxxiao
@LastEditTime: 2020-04-19 16:47:50
'''


class Solution:
    def __init__(self):
        self.num_value = {
                '2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']
            }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if digits == "":
            return []
        out = ['']
        for i in range(len(digits)):
            out = self.compostion(digits[i], out)
        return out

    def compostion(self, digit, out):
        k = [j+i for i in self.num_value[digit] for j in out]
        return k


    def letterCombinations_backtrack(self, digits):
        def backtrack(path, next_digits):
            if len(next_digits) == 0:
                output.append(path)
            else:
                for letter in self.num_value[next_digits[0]]:
                    backtrack(path + letter, next_digits[1:])
        output = []
        if digits:
            backtrack("", digits)
        return output


input_nums = "23"

output = Solution().letterCombinations_backtrack(input_nums)
print(output)
