# 编写一个函数来查找字符串数组中的最长公共前缀。 
# 
#  如果不存在公共前缀，返回空字符串 ""。 
# 
#  示例 1: 
# 
#  输入: ["flower","flow","flight"]
# 输出: "fl"
#  
# 
#  示例 2: 
# 
#  输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#  
# 
#  说明: 
# 
#  所有输入只包含小写字母 a-z 。 
#  Related Topics 字符串


# leetcode submit region begin(Prohibit modification and deletion)

# No.01
"""
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        strs.sort(key=len)
        if not strs or not strs[0]:
            return ""
        elif len(set(strs)) == 1:
            return strs[0]
        else:
            base_str = strs[0]
            for index, alphabet in enumerate(base_str):
                for compare_str in strs[1:]:
                    if compare_str[index] != alphabet:
                        return strs[0][:index]
            return base_str
"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs or not strs[0]:
            return ""
        else:
            strs.sort(key=len)
            s = strs[0]
            for i in range(1, len(strs)):
                while not strs[i].startswith(s):
                    s = s[:-1]
            return s

# leetcode submit region end(Prohibit modification and deletion)

# [], [""], ["a"], ["a", "a"], ["abc", "abd", "abk"], ["ab", "sdf", ""]

# a = Solution()
# print(a.longestCommonPrefix(["flower", "flow", "flight"]))
