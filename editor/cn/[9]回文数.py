# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。 
# 
#  示例 1: 
# 
#  输入: 121
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#  
# 
#  示例 3: 
# 
#  输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
#  
# 
#  进阶: 
# 
#  你能不将整数转为字符串来解决这个问题吗？ 
#  Related Topics 数学


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x_str = str(x)
            devide_two = len(x_str) // 2
            if len(x_str) % 2:
                if x_str[:devide_two][::-1] == x_str[devide_two + 1:]:
                    return True
            else:
                if x_str[:devide_two][::-1] == x_str[devide_two:]:
                    return True
            return False

# leetcode submit region end(Prohibit modification and deletion)
