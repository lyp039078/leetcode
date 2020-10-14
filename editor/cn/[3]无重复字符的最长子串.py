# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。 
# 
#  示例 1: 
# 
#  输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window 
#  👍 4457 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 思路1(不可行)： 增加一个临时变量a，逐个把字符串中的字母移入a中，但发现准备移入的字母已存在时，计算临时变量长度length，再清空a。在此过程中，获取最大值的length
    # 测试用例:"dvdf" 期望结果：3 按上述思路测试为2

    # 思路2： 在思路1上，发现有重复的字母时，应只去除首个字母再重新遍历 --> 即，不可使用转移的方式，应该时每处理完一次去去掉首字母再重复处理步骤
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        while len(s) > length:  # 通过剩余长度来判断，减少计算次数，且遍历到s最后一个时，不会走break
            a = ""
            for letter in s:
                if letter not in a:
                    a += letter
                    length = max(len(a), length)
                else:
                    s = s[1:]
                    break
        return length
    """
    # 思路3——整体移动：增加一个临时变量a， 遍历s中的字母，并增加到a中。当发现重复时，去除a中重复字母前面内容(包括重复字母)，增加s的遍历字母。
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        a = ""
        for letter in s:
            if letter not in a:
                a += letter
            else:
                a = a[a.index(letter)+1:] + letter
            length = max(len(a), length)
        return length
# leetcode submit region end(Prohibit modification and deletion)
