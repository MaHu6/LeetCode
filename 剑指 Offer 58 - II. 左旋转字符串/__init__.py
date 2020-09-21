from Utils.common import run_time

"""
题目
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

示例 1：

输入: s = "abcdefg", k = 2
输出: "cdefgab"

"""

"""
reverseLeftWords1 ： 切片
reverseLeftWords2：列表遍历拼接

"""


class Solution:
    @run_time
    def reverseLeftWords1(self, s: str, n: int) -> str:
        return s[n:] + s[:n]

    @run_time
    def reverseLeftWords2(self, s: str, n: int) -> str:
        res = []
        # for i in range(n, len(s)):
        #     res.append(s[i])
        #
        # for i in range(n):
        #     res.append(s[i])

        # 取余数遍历
        s_len = len(s)
        for i in range(n, s_len + n):
            res.append(s[i % s_len])

        return "".join(res)


if __name__ == '__main__':
    target_str = "abcdefg"
    target_num = 2

    s = Solution()
    print(s.reverseLeftWords1(target_str, target_num))
    print(s.reverseLeftWords2(target_str, target_num))
