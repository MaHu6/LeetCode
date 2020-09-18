from copy import deepcopy
from typing import List

from Utils.common import run_time

"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""


class Solution:
    @run_time
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path: List[int], nums):

            # print(f"path : {path}")
            # print(f"nums : {nums}")

            if not nums:
                # 树深度遍历到底
                if path in res:
                    return
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

    @run_time
    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path: List[int], nums: List[int]):
            if not nums:
                if path in res:
                    return

                res.append(path)
                return

            for i in range(len(nums)):
                path.append(nums[i])

                backtrack(deepcopy(path), nums[:i] + nums[(i + 1):])
                # backtrack(path[:], nums[:i] + nums[(i + 1):])

                path.pop()

        backtrack([], nums)

        return res


if __name__ == '__main__':
    nums = [1, 1, 2]
    s = Solution()
    print(s.permuteUnique2(nums))
