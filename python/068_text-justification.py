#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start


class Solution:
    def fullJustify(self, words, maxWidth):
        res, cur, num_of_letters = [], [], 0
        # 遍历词表
        for w in words:
            # num_of_letters：cur里的单词长度，len(w)新添加单词长度，len(cur):指单词数也就是词和词之间的空格
            if num_of_letters + len(w) + len(cur) > maxWidth:
                # 需要添的空格数目
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]



words = ["This", "is", "an", "example", "of", "text", "justification."]
Solution().fullJustify(words, 16)

# @lc code=end
