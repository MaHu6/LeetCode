from typing import List

from binarytree import Node as TreeNode

from Utils.common import run_time

"""
题目：
给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：

二叉树的根是数组中的最大元素。
左子树是通过数组中最大值左边部分构造出的最大二叉树。
右子树是通过数组中最大值右边部分构造出的最大二叉树。
通过给定的数组构建最大二叉树，并且输出这个树的根节点。

示例 ：

输入：[3,2,1,6,0,5]
输出：返回下面这棵树的根节点：

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1


"""

"""
二叉树的中序遍历
"""


class Solution:
    @run_time
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        if len(nums) == 1:
            return TreeNode(nums[0])

        if not nums:
            return

        max_index = nums.index(max(nums))
        current_val = nums[max_index]
        current_node = TreeNode(current_val)

        left_nums = nums[:max_index]
        right_nums = nums[max_index + 1:]

        if left_nums:
            current_node.left = self.constructMaximumBinaryTree(left_nums)

        if right_nums:
            current_node.right = self.constructMaximumBinaryTree(right_nums)

        return current_node


if __name__ == '__main__':
    target_nums = [3, 2, 1, 6, 0, 5]

    s = Solution()
    print(s.constructMaximumBinaryTree(target_nums))
    print(s.constructMaximumBinaryTree([]))
