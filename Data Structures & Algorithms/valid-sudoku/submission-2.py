class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r=defaultdict(set)
        c=defaultdict(set)
        s=defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board)):
                value=board[row][col]
                if value == ".":
                    continue
                if value in r[row] or value in c[col] or value in s[row//3, col//3]:
                    return False
                r[row].add(value)
                c[col].add(value)
                s[row//3, col//3].add(value)
        return True                