from typing import List

from Utils.common import run_time

"""
前序遍历:打印-左-右
中序遍历:左-打印-右
后序遍历:左-右-打印
"""

"""
题目：
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归方式
    @run_time
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return
            # 按照 左-打印-右的方式遍历
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        return res

    # 迭代方式
    @run_time
    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        res = []
        stacks = []

        while root or stacks:
            if root:
                # 不断往左子树方向走，每走一次就将当前节点保存到栈中
                # 这是模拟递归的调用
                stacks.append(root)
                root = root.left

            else:
                # 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
                # 然后转向右边节点，继续上面整个过程
                tmp = stacks.pop()
                res.append(tmp.val)
                root = tmp.right

        return res


def initNode() -> TreeNode:
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    return a


if __name__ == '__main__':
    root = initNode()

    s = Solution()
    print(s.inorderTraversal(root))
    print(s.inorderTraversal2(root))
