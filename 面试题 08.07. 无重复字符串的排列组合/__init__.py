from copy import deepcopy
from typing import List

from Utils.common import run_time

"""
题目：
无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。

示例1:

 输入：S = "qwe"
 输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]

"""

"""
回溯法
"""


class Solution:
    @run_time
    def permutation(self, S: str) -> List[str]:
        res = []

        def backtrack(path: str, strs: str):
            if strs == "":
                res.append(path)

            for i in range(len(strs)):
                path += strs[i]
                backtrack(deepcopy(path), strs[:i] + strs[i + 1:])

                path = path[:len(path) - 1]

        backtrack('', S)

        return res


if __name__ == '__main__':
    S = "abcd"
    s = Solution()
    print(s.permutation(S))
