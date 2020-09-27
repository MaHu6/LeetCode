from typing import List

from Utils.common import run_time

"""
题目
有个内含单词的超大文本文件，给定任意两个单词，找出在这个文件中这两个单词的最短距离(相隔单词数)

输入：words = ["I","am","a","student","from","a","university","in","a","city"],
word1 = "a", 
word2 = "student"

输出：1

"""


class Solution:
    @run_time
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:

        i, ans = 0, len(words)

        for j, word in enumerate(words):
            if word == word1 or word == word2:
                # 遇到两个词之一
                if word != words[i] and (words[i] == word1 or words[i] == word2):
                    # i一定指向word1或word2,但i=0时不一定，所以加入条件(words[i] == word1 or words[i] == word2)
                    ans = min(ans, j - i)
                    print(ans)

                i = j

        return ans


if __name__ == '__main__':
    words = ["I", "am", "a", "student", "from", "a", "university", "in", "a", "city"]
    word1 = "a"
    word2 = "student"

    s = Solution()
    print(s.findClosest(words, word1, word2))
