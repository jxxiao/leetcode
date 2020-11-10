'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2020-04-07 17:06:09
@LastEditors: jxxiao
@LastEditTime: 2020-04-07 17:07:23
'''
#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#
# https://leetcode-cn.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (32.14%)
# Likes:    137
# Dislikes: 0
# Total Accepted:    8.2K
# Total Submissions: 26K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord
# 的最短转换序列。转换需遵循如下规则：
#
#
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
#
#
# 说明:
#
#
# 如果不存在这样的转换序列，返回一个空列表。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
#
#
# 示例 1:
#
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# 输出:
# [
# ⁠ ["hit","hot","dot","dog","cog"],
# ["hit","hot","lot","log","cog"]
# ]
#
#
# 示例 2:
#
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# 输出: []
#
# 解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
#
#

# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        def nextWords(word, path):
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    nextWord = word[:i] + c + word[i + 1:]
                    if nextWord in wordSet and nextWord not in path:
                        yield nextWord
        path = []
        res = []
        wordSet = set(wordList)
        queue = collections.deque([(beginWord, [beginWord], 1)])
        miniStep = float("inf")

        while queue:
            newqueue = queue
            queue = collections.deque()
            while newqueue:
                word, path, step = newqueue.popleft()
                if word == endWord:
                    if step < miniStep:
                        miniStep = step
                        res.clear()
                        res.append(path)
                    elif step == miniStep:
                        res.append(path)
                for nextWord in nextWords(word, path):
                    queue.append((nextWord, path + [nextWord], step + 1))

        return res
# @lc code=end
