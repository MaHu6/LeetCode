import datetime
import time
from functools import wraps
from typing import List

from binarytree import Node as TreeNode


def run_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_start_time = time.time()
        # print(f'{func.__name__} start ...')
        ret = func(*args, **kwargs)
        # print(f'{func.__name__} end ...')
        print(f'Run Time Of Func -> {func.__name__} is : {format_runtime(time.time() - func_start_time)}')

        return ret

    return wrapper


def format_runtime(t) -> str:
    return f"{datetime.timedelta(seconds=t)}"


# 列表转二叉树
def list2BinaryTree(root: TreeNode, nums: List, i: int):
    if i < len(nums):
        if nums[i] == None:  # 节点是空的时候 返回空
            return None
        else:
            root = TreeNode(nums[i])
            root.left = list2BinaryTree(root.left, nums, i * 2 + 1)
            root.right = list2BinaryTree(root.right, nums, i * 2 + 2)
        return root

    return root
