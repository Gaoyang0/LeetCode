from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 一次遍历
        flag_map = {"row": {}, "col": {}, "3*3": {}}
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if i not in flag_map["row"]:
                    flag_map["row"].update({i:set(board[i][j])})
                else:
                    if board[i][j] in flag_map["row"][i]:
                        print(i, j, "r")
                        return False
                    else:
                        flag_map["row"][i].add(board[i][j])

                if j not in flag_map["col"]:
                    flag_map["col"].update({j:set(board[i][j])})
                else:
                    if board[i][j] in flag_map["col"][j]:
                        print(i, j, "c")
                        return False
                    else:
                        flag_map["col"][j].add(board[i][j])

                # 3*3的编号（0-8）
                k = (i//3)*3 + j//3
                if k not in flag_map["3*3"]:
                    flag_map["3*3"].update({k: set(board[i][j])})
                else:
                    if board[i][j] in flag_map["3*3"][k]:
                        print(i, j, "33")
                        return False
                    else:
                        flag_map["3*3"][k].add(board[i][j])
        return True


s = Solution()

print(s.isValidSudoku(
[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))

