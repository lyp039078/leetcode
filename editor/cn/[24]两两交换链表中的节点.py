# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。 
# 
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#  
# 
#  示例: 
# 
#  给定 1->2->3->4, 你应该返回 2->1->4->3.
#  
#  Related Topics 链表 
#  👍 651 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # print("head: %s" % head)
        old_list = []
        while head:
            old_list.append(head.val)
            head = head.next
        # print("old_list: %s" % old_list)
        # head 为None时， old_list为空，直接返回head
        if not old_list:
            return head
        for i in range(0, len(old_list), 2):
            if i < len(old_list)-1:
                old_list[i], old_list[i+1] = old_list[i+1], old_list[i]
        new_list_node = ListNode(old_list.pop(), None)
        while old_list:
            new_list_node = ListNode(old_list.pop(), new_list_node)
        return new_list_node
# leetcode submit region end(Prohibit modification and deletion)

