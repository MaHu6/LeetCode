from typing import List

from Utils.common import run_time

"""
题目：
三枚石子放置在数轴上，位置分别为 a，b，c。

每一回合，我们假设这三枚石子当前分别位于位置 x, y, z 且 x < y < z。从位置 x 或者是位置 z 拿起一枚石子，并将该石子移动到某一整数位置 k 处，其中 x < k < z 且 k != y。

当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。

要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 以长度为 2 的数组形式返回答案：answer = [minimum_moves, maximum_moves]


示例 1：

输入：a = 1, b = 2, c = 5
输出：[1, 2]
解释：将石子从 5 移动到 4 再移动到 3，或者我们可以直接将石子移动到 3。

示例 2：

输入：a = 4, b = 3, c = 2
输出：[0, 0]
解释：我们无法进行任何移动。

"""

"""
情况 1 ：
        x,y,z 连续， [0,0]

情况 2 ：
        x,y,z 至少有一个间隔，将远处的数移过来，最小移动 minimum_moves 为 1
        x,*,y,z
        x,y,*,z

情况 3 ：
        x,y,z 两个间隔都大于 1 ，则至少移动 2 次，minimum_moves 为 2 
        x,*...*,y,*...*,z
        那么 情况 2 和 情况 3 的最大移动次数 maximum_moves = （y-x）+ (z-y) - 2

"""


class Solution:
    @run_time
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        # 排序
        tmp = [a, b, c]
        tmp.sort()
        x, y, z = tmp[0], tmp[1], tmp[2]

        if x + 1 == y and y + 1 == z:  # abc 连续
            return [0, 0]
        else:
            if y - x == 2 or z - y == 2 or (x + 1 == y or y + 1 == z):  # 中间隔着 1 个或者 2 个挨着
                minimum_moves = 1
            else:
                minimum_moves = 2

            maximum_moves = (y - x) + (z - y) - 2

            return [minimum_moves, maximum_moves]


if __name__ == '__main__':
    s = Solution()
    print(s.numMovesStones(3, 4, 5))
    print(s.numMovesStones(1, 2, 9))
