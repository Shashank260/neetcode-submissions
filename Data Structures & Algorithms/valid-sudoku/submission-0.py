class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        columns=defaultdict(set)
        boxes=defaultdict(set)
        for i in range(0,9):
            for j in range(0,9):
                v=board[i][j]
                if v!='.':
                    if v in rows[i]:
                        return False
                    if v in columns[j]:
                        return False
                    if v in boxes[(i//3,j//3)]:
                        return False
                    rows[i].add(v)
                    columns[j].add(v)
                    boxes[(i//3,j//3)].add(v)
        return True      

                
            
            
