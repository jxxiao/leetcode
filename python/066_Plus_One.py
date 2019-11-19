class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)):
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            digits[~i] = 0
        return [1] + [0] * len(digits)

    def plusOnebyStr(self, digits):
        result = []
        for i in str(int(''.join(str(i) for i in digits)) + 1):
            result.append(int(i))
        return result


digits = [1, 8, 9]
print(Solution().plusOne(digits))
