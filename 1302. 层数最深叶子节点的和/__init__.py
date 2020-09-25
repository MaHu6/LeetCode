from typing import List

from binarytree import Node as TreeNode

from Utils.common import list2BinaryTree

"""
给你一棵二叉树，请你返回层数最深的叶子节点的和。

      __1
     /   \
    2     3
   / \     \
  4   5     6
 /           \
7             8


15



"""

"""
depth > maxDepth，更新maxDepth（ ⚠️每层结果应保留node.val，不然第一个最深节点会被漏掉）
depth == maxDepth，计入结果


"""


class Solution:
    def __init__(self):
        self.max_depth = -1
        self.res = 0

    # 递归
    def deepestLeavesSum(self, root: TreeNode) -> int:

        def dfs(root: TreeNode, depth: int):
            if not root:
                return

            if depth > self.max_depth:
                self.res = root.val
                self.max_depth = depth

            elif depth == self.max_depth:  # 最外层
                self.res += root.val

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 0)

        return self.res


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, None, None, 8]

    target_node = list2BinaryTree(None, nums, 0)
    print(target_node)

    s = Solution()
    print(s.deepestLeavesSum(target_node))
