from typing import List

from Utils.common import list2BinaryTree, run_time
from binarytree import Node as TreeNode

"""
题目：
给定一个二叉树，返回它的 前序 遍历。
输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [1,2,3]
"""

"""
前序：根 左 右

"""


class Solution:
    # 递归
    @run_time
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(root: TreeNode):
            if not root:
                return

            res.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return res

    # 迭代
    @run_time
    def preorderTraversal2(self, root: TreeNode) -> List[int]:

        stack, output = [root, ], []

        while stack:
            root = stack.pop()

            if root:
                output.append(root.val)

                """
                先压入 right,再压入 left，，pop 的时候，left 就会先出来
                """
                if root.right:
                    stack.append(root.right)

                if root.left:
                    stack.append(root.left)

        return output


if __name__ == '__main__':
    nums = [3, 1, 2]
    target_node = list2BinaryTree(None, nums, 0)
    print(target_node)

    s = Solution()
    print(s.preorderTraversal(target_node))
    print(s.preorderTraversal2(target_node))
