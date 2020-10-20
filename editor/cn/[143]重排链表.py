# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ， 
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→… 
# 
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#  示例 1: 
# 
#  给定链表 1->2->3->4, 重新排列为 1->4->2->3. 
# 
#  示例 2: 
# 
#  给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3. 
#  Related Topics 链表 
#  👍 337 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    '''
    # 思路1： 将链表转为列表，重新排序，再重新转回链表
    # 要求应该是在原链表上修改，新生成的列表和原列表不一样，无法通过
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        print("head:{}".format(head))
        head_list = [head.val]
        while head.next:
            head_list.append(head.next.val)
            head = head.next
        print("head_list: {}".format(head_list))
        new_list = []
        for index in range(len(head_list)):
            if index % 2:
                new_list.append(head_list.pop())
            else:
                new_list.append(head_list.pop(0))
        print("new_list: {}".format(new_list))
        head = None
        for index in range(len(new_list)):
            head = ListNode(new_list.pop(), head)
        print("head: {}".format(head))
    '''

    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        head_list = []
        node = head
        while node:
            head_list.append(node)
            node = node.next

        i, j = 0, len(head_list) - 1
        while i < j:
            head_list[i].next = head_list[j]
            i += 1
            if i == j:
                break
            head_list[j].next = head_list[i]
            j -= 1
        head_list[j].next = None
# leetcode submit region end(Prohibit modification and deletion)
