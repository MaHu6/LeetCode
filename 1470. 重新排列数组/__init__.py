from typing import List

from Utils.common import run_time

"""
shuffle

    通过in-place swap的方法做到O(1)空间O(n)时间。
    
    每个"nums[i]"都有一个“目标”index。
    例如对于8个数的nums, "nums[0]"想去"0", "nums[4]"想去"1", "nums[1]"想去"2", "nums[5]"想去"3", "nums[2]"想去"4"...
    
    in-place把nums[i] swap到它想去的index，把swap走的数标记为负数，并把swap回来的数继续"原地"swap出去，
    直到swap回来的数的目标index就是“i”自己，然后才增加"i"并继续过下一个“i”。
    
    遇到nums[i]是负数就说明nums[i]已经在之前的swap中到达了目前位置，因此跳过。
    
    所有的i都过好后nums就是正确的顺序，别忘了最后再过一遍把所有的负数变回正数。
    
    由于每个nums[i]只会被标记1次负数，因此时间复杂度是O(n)


shuffle2 
    分为前后两个数组，依次装填

"""


class Solution:
    @run_time
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        getDesIndex = lambda i: i * 2 if i < n else (i - n) * 2 + 1

        for i in range(2 * n):
            j = i
            while nums[i] >= 0:
                j = getDesIndex(j)
                nums[i], nums[j] = nums[j], -nums[i]

        for i in range(2 * n):
            nums[i] = -nums[i]

        return nums

    @run_time
    def shuffle2(self, nums: List[int], n: int) -> List[int]:

        res_nums = []
        x = nums[:n]
        y = nums[n:]

        for i in range(n):
            res_nums.append(x[i])
            res_nums.append(y[i])

        return res_nums


if __name__ == '__main__':
    nums = [2, 5, 1, 3, 4, 7, 9, 6]
    n = 4

    print(nums)
    s = Solution()
    print(s.shuffle(nums, n))

    nums = [2, 5, 1, 3, 4, 7, 9, 6]

    print(s.shuffle2(nums, n))
