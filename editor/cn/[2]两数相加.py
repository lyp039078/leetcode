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


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """

        :param l1:
        :param l2:
        :return:
        """
        # print(dir(l1))
        # print(l1)
        # print(l1.val)
        # print(repr(l1.var()))
        # print(l1.next())
        l1_list = []
        l2_list = []
        res_list = []
        if not l1 or not l2:
            return l1 if not l1 else l2

        while l1 is not None:
            l1_list.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            l2_list.append(l2.val)
            l2 = l2.next
        l1_number = int("".join(map(str, reversed(l1_list))))
        l2_number = int("".join(map(str, reversed(l2_list))))
        res_number = l1_number + l2_number
        # print("res_number: {}".format(res_number))
        res_list = [int(i) for i in str(res_number)[::-1]]
        # print("res_list: %s" % res_list)

        res_list_node = None
        while res_list:
            res_list_node = ListNode(res_list.pop(), res_list_node)
            # print("res_list_node: %s" % res_list_node)

        return res_list_node


# leetcode submit region end(Prohibit modification and deletion)
