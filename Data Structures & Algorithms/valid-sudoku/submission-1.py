class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(9)]
        col=[set()  for _ in range(9)]
        box=[set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                    
                num=board[r][c]
                if num in row[r]:
                    return False
                row[r].add(num)

                if num in col[c]:
                    return False
                col[c].add(num)

                b=(r//3)*3+(c//3)
                if num in box[b]:
                    return False
                box[b].add(num)
        return True