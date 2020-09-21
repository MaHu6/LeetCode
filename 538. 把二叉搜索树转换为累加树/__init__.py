from Utils.common import run_time
from Utils.var import TreeNode

"""
题目：
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

 

例如：

输入: 原始二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13

"""

"""
二叉搜索树是一棵空树，或者是具有下列性质的二叉树：

若它的左子树不空，则左子树上所有节点的值均小于它的根节点的值；

若它的右子树不空，则右子树上所有节点的值均大于它的根节点的值；

它的左、右子树也分别为二叉搜索树。

由这样的性质我们可以发现，二叉搜索树的中序遍历是一个单调递增的有序序列。如果我们反序地中序遍历该二叉搜索树，即可得到一个单调递减的有序序列。
中序遍历：5，2，13
反序中序遍历： 13，5，2

反序中序遍历该二叉搜索树，记录过程中的节点值之和，并不断更新当前遍历到的节点的节点值，即可得到题目要求的累加树。

"""


class Solution:
    @run_time
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode):
            nonlocal total

            if root:
                dfs(root.right)
                total += root.val
                root.val = total
                dfs(root.left)

        total = 0

        dfs(root)

        return root


def initNode() -> TreeNode:
    a = TreeNode(5)
    b = TreeNode(2)
    c = TreeNode(13)

    a.left = b
    a.right = c

    return a


if __name__ == '__main__':
    targetNode = initNode()
    s = Solution()
    s.convertBST(targetNode)
