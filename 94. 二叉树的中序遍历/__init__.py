from typing import List

from Utils.common import run_time, list2BinaryTree
from binarytree import Node as TreeNode

"""
A：根节点、B：左节点、C：右节点，
    A
   / \
  B   C

前序顺序是ABC（根节点排最先，然后同级先左后右）；
中序顺序是BAC(先左后根最后右）；
后序顺序是BCA（先左后右最后根）。

           a
          / \
         b   c
        / \  / \
       d  e  f  g


前序：根左右  a b d e c f g

中序：左根右  d b e a f c g

后序：左右根  d e b f g c a



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

    nums = [1, 2, 3, 4, 5, 6, 7]
    target_node = list2BinaryTree(None, nums, 0)
    print(target_node)

    print(s.inorderTraversal(target_node))
    print(s.inorderTraversal2(target_node))
