# 给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不
# 是 4 次，则需要在最终答案中包含该字符 3 次。 
# 
#  你可以按任意顺序返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  输入：["bella","label","roller"]
# 输出：["e","l","l"]
#  
# 
#  示例 2： 
# 
#  输入：["cool","lock","cook"]
# 输出：["c","o"]
#  
#
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 100 
#  1 <= A[i].length <= 100 
#  A[i][j] 是小写字母 
#  
#  Related Topics 数组 哈希表 
#  👍 114 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # 非重复遍历列表中第一个字符串，计算所有字符串中该字母出现的次数并去最小值，再各自删除该字母
    def commonChars(self, A):
            """
            :type A: List[str]
            :rtype: List[str]
            """
            first_value_set = set(A[0])
            res_list = []
            for letter in first_value_set:
                # 计算出现次数的最小值
                min_count = A[0].count(letter)
                for index in range(len(A)):
                    if A[index].count(letter) < min_count:
                        min_count = A[index].count(letter)
                    # 删除字母
                    A[index] = A[index].replace(letter, "")
                # 添加 字母*出现的最小次数
                res_list.extend(letter*min_count)
            return res_list


# leetcode submit region end(Prohibit modification and deletion)
