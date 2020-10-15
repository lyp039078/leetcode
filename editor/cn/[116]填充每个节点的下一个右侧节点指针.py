# 给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下： 
# 
#  struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# } 
# 
#  填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。 
# 
#  初始状态下，所有 next 指针都被设置为 NULL。 
# 
#  
# 
#  示例： 
# 
#  
# 
#  输入：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"ri
# ght":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right
# ":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left"
# :null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":nu
# ll,"next":null,"right":null,"val":7},"val":3},"val":1}
# 
# 输出：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4
# ","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next"
# :null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":
# null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":
# "6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"va
# l":1}
# 
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
#  
# 
#  
# 
#  提示： 
# 
#  
#  你只能使用常量级额外空间。 
#  使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。 
#  
#  Related Topics 树 深度优先搜索 
#  👍 311 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # 参考官方题解：
    #          1
    #       /     \
    #      2   ->   3
    #    /  \      /  \
    #   4 -> 5 -> 6 -> 7
    # 1. root 为None 时，直接返回root
    # 2. 从根节点开始，节点为head
    # 3. 左分叉的next： 其head.left.next = head.right
    # 4. 右分叉的next： 当head.next存在时，head.right.next = head.next.left
    # 5. 对于每层的最右侧，不做变化，初始就是None
    def connect(self, root: 'Node') -> 'Node':
        # 整个二叉树为None时，直接返回
        if not root:
            return root

        # leftmost：每层最左侧的节点，从根节点开始，
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                # 左分叉的next
                head.left.next = head.right
                if head.next:
                    # 右分叉的next
                    head.right.next = head.next.left
                # 处理当前节点的next，指针向后移动(当前节点的next)
                head = head.next
            # 当前层处理完，指针移到下一层
            leftmost = leftmost.left
        return root

# leetcode submit region end(Prohibit modification and deletion)
"""
Node_value = {
    "$id": "1",
    "left": {
        "$id": "2",
        "left": {
            "$id": "3",
            "left": None,
            "next": None,
            "right": None,
            "val": 4
        },
        "next": None,
        "right": {
            "$id": "4",
            "left": None,
            "next": None,
            "right": None,
            "val": 5
        },
        "val": 2
    },
    "next": None,
    "right": {
        "$id": "5",
        "left": {
            "$id": "6",
            "left": None,
            "next": None,
            "right": None,
            "val": 6
        },
        "next": None,
        "right": {
            "$id": "7",
            "left": None,
            "next": None,
            "right": None,
            "val": 7
        },
        "val": 3
    },
    "val": 1}
"""