'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2020-02-25 23:18:54
@LastEditors: jxxiao
@LastEditTime: 2020-03-15 00:37:06
'''
#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
# https://leetcode.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (20.40%)
# Likes:    1462
# Dislikes: 220
# Total Accepted:    160.4K
# Total Submissions: 783.9K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# all shortest transformation sequence(s) from beginWord to endWord, such
# that:
#
#
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
#
#
# Note:
#
#
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
#
#
# Example 1:
#
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output:
# [
# ⁠ ["hit","hot","dot","dog","cog"],
# ["hit","hot","lot","log","cog"]
# ]
#
#
# Example 2:
#
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: []
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
#
#
#
#
#
#

# @lc code=start

import collections
import string
import copy


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        def nextWords(word, path, uncleNode):
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    nextWord = word[:i] + c + word[i + 1:]
                    if nextWord in wordSet and nextWord not in path and nextWord not in uncleNode:
                        yield nextWord
        path = []
        res = []
        wordSet = set(wordList)
        queue = collections.deque([(beginWord, [beginWord], 1)])
        miniStep = float("inf")
        uncleNode = []

        while queue:
            newqueue = queue
            queue = collections.deque()
            tempqueue = copy.deepcopy(newqueue)
            while tempqueue:
                Node, _, _ = tempqueue.popleft()
                uncleNode.append(Node)

            while newqueue:
                word, path, step = newqueue.popleft()
                if word == endWord:
                    if step < miniStep:
                        miniStep = step
                        res.clear()
                        res.append(path)
                    elif step == miniStep:
                        res.append(path)
                for nextWord in nextWords(word, path, uncleNode):
                    queue.append((nextWord, path + [nextWord], step + 1))

        return res


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]

print(Solution().findLadders(beginWord, endWord, wordList))

# @lc code=end
