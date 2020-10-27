# 请判断一个链表是否为回文链表。 
# 
#  示例 1: 
# 
#  输入: 1->2
# 输出: false 
# 
#  示例 2: 
# 
#  输入: 1->2->2->1
# 输出: true
#  
# 
#  进阶： 
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
#  Related Topics 链表 双指针 
#  👍 722 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 思路1： 转换为列表，通过索引来判断 ==> 等待结果超时
    # 此处必须用新的变量接收head,不能直接在head上处理(head好像是不可变)
    # 循环判断的时候，可以通过双索引(双索引来判断):
    # start = 0
    # end = len(node_list)-1
    # while start < end:
    #     if node_list[start] !- node_list[end]:
    #         return False
    #     start += 1
    #     end -= 1
    # return True
    def isPalindrome(self, head: ListNode) -> bool:
        node_list = []
        node = head
        while node:
            node_list.append(node.val)
            node = node.next
        for index in range(len(node_list) // 2):
            if node_list[index] != node_list[-(index + 1)]:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
