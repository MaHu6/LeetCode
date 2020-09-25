from typing import List

from Utils.common import run_time, list2BinaryTree
from binarytree import Node as TreeNode

"""
题目：
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]

"""

"""
后序：左 右 根
"""


class Solution:
    # 递归
    @run_time
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(root: TreeNode):
            if not root:
                return

            dfs(root.left)
            dfs(root.right)
            res.append(root.val)

        dfs(root)

        return res

    # 迭代
    @run_time
    def postorderTraversal2(self, root: TreeNode) -> List[int]:

        stacks, res = [root, ], []

        while stacks:
            root = stacks.pop()

            if root:
                res.append(root.val)

                # 先压入 left ,再压入 right, right 先弹出，最后反序，前变后
                if root.left:
                    stacks.append(root.left)

                if root.right:
                    stacks.append(root.right)

        print("*" * 100)
        print(res)
        return res[::-1]


if __name__ == '__main__':
    nums = [1, 4, 2, None, 8, 3]
    target_node = list2BinaryTree(None, nums, 0)
    print(target_node)

    s = Solution()

    print(s.postorderTraversal(target_node))
    print(s.postorderTraversal2(target_node))
