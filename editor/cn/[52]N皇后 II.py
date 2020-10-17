# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  
# 
#  上图为 8 皇后问题的一种解法。 
# 
#  给定一个整数 n，返回 n 皇后不同的解决方案的数量。 
# 
#  示例: 
# 
#  输入: 4
# 输出: 2
# 解释: 4 皇后问题存在如下两个不同的解法。
# [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
#  
# 
#  
# 
#  提示： 
# 
#  
#  皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或 N
# -1 步，可进可退。（引用自 百度百科 - 皇后 ） 
#  
#  Related Topics 回溯算法 
#  👍 178 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 思路1：
    # - 指定一个n*n 的矩阵
    # - 选定一个点(i,j)后，去除矩阵中(i, j) 以及以下点：
    # -     同一列： (i, *)
    # -     同一行： (*, j)
    # -     左斜： (i-k, j+k) k=1,2,3...  i-k>=0, j+k<n
    # -     右斜： (i+k, j-k) k=1,2,3...  i+k<n, j-k>=0
    # - 选取下一个点，重复上面步骤
    # - 可选点为0且选取的点<n时，为失败方案；选取点达到8个时，记作一次成功

    # 思路2(参考官方方法):
    # - 左斜： i+j的值时一样的；右斜： 相减的值时一样的
    # - 用集合来分别存储，已选点的列号 j， 已选点左斜方向之和i+j， 已选点右斜方向之差 i-j
    # - 从上往下遍历，并判断点对应的值是否存在于三个集合中

    def totalNQueens(self, n: int) -> int:
        def get_count(line_index: int) -> int:
            # 结束递归条件：递归完最后一行时
            if line_index == n:
                return 1
            count = 0
            for columns_index in range(n):
                # 当判断当前点位不可选时，跳到下一个点
                if columns_index in columns or line_index + columns_index in diagonal_sum or line_index - columns_index in diagonal_diff:
                    continue
                # 当前点位可使用，将该点位相关添加的集合中
                columns.add(columns_index)
                diagonal_sum.add(line_index + columns_index)
                diagonal_diff.add(line_index - columns_index)
                count += get_count(line_index + 1)
                # 三个集合需要恢复到此递归前状态，便于下次的for循环
                columns.remove(columns_index)
                diagonal_sum.remove(line_index + columns_index)
                diagonal_diff.remove(line_index - columns_index)
            return count

        columns = set()
        diagonal_sum = set()
        diagonal_diff = set()
        return get_count(0)
# leetcode submit region end(Prohibit modification and deletion)
