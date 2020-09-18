from copy import deepcopy
from typing import List

from Utils.common import run_time

"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]


"""

"""


深度遍历
    1               2               3
2       3       1       3       1       2
3       2       3       1       2       1           


"""


class Solution:
    # 回溯法，深度优先遍历

    @run_time
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path: List[int], nums):

            # print(f"path : {path}")
            # print(f"nums : {nums}")

            if not nums:
                # 树深度遍历到底
                res.append(path)
                return

            for i in range(len(nums)):
                # print(f"for -> path : {path}")
                # print(f"for -> nums : {nums}")

                # 将当前数加入 path
                path.append(nums[i])

                #
                backtrack(deepcopy(path), nums[:i] + nums[i + 1:])

                # print(f"Before Cancel path : {path}")
                # 撤销
                path.pop()
                # print(f"After Cancel path : {path}")

        backtrack([], nums)

        return res


if __name__ == '__main__':
    nums = [1, 2, 3]

    s = Solution()
    print(s.permute(nums))
