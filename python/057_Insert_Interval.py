class Solution:
    def insert(self, intervals, newInterval):
        start, end = newInterval[0], newInterval[-1]
        left = [i for i in intervals if i[-1] < start]
        right = [i for i in intervals if i[0] > end]
        if left + right != intervals:
            start = min(start, intervals[len(left)][0])
            end = max(end, intervals[~len(right)][-1])
        return left + [[start, end]] + right


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]

print(Solution().insert(intervals, newInterval))
