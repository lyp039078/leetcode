# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。 
# 
#  如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。 
# 
#  您可以假设除了数字 0 之外，这两个数都不会以 0 开头。 
# 
#  示例： 
# 
#  输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#  
#  Related Topics 链表 数学 
#  👍 5085 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         """
#
#         :param l1:
#         :param l2:
#         :return:
#         """
#         l1_list = []
#         l2_list = []
#         res_list = []
#         if not l1 or not l2:
#             return l1 if not l1 else l2
#
#         while l1 is not None:
#             l1_list.append(l1.val)
#             l1 = l1.next
#         while l2 is not None:
#             l2_list.append(l2.val)
#             l2 = l2.next
#         l1_number = int("".join(map(str, reversed(l1_list))))
#         l2_number = int("".join(map(str, reversed(l2_list))))
#         res_number = l1_number + l2_number
#         res_list = [int(i) for i in str(res_number)[::-1]]
#
#         res_list_node = None
#         while res_list:
#             res_list_node = ListNode(res_list.pop(), res_list_node)
#
#         return res_list_node

# 12:22	info
#     解答成功:
#     执行耗时:56 ms,击败了95.15% 的Python用户
#     内存消耗:13.4 MB,击败了5.39% 的Python用户


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s = 0
        res_list_node = temp_node = ListNode()
        while l1 or l2 or s:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            temp_node.next = ListNode(val=s % 10)
            temp_node = temp_node.next
            s //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res_list_node.next
        
# leetcode submit region end(Prohibit modification and deletion)


# 13:28	info
# 			解答成功:
# 			执行耗时:80 ms,击败了52.41% 的Python3用户
# 			内存消耗:13.7 MB,击败了5.36% 的Python3用户