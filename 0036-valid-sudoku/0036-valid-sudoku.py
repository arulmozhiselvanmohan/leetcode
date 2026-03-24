class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        search_map = {}

        for row in range(0,len(board)):
            search_map = {}
            for col in range(0,len(board[row])):
                 
                if board[row][col] != "." and board[row][col] in search_map:
                    return False
                search_map[board[row][col]] = True
        
        
        for row in range(0,len(board)):
            search_map = {}
            for col in range(0,len(board[row])):
                if board[col][row] !="." and board[col][row] in search_map:
                    return False
                search_map[board[col][row]] = True


        for row in range(0,len(board),3):
            for col in range (0, len(board),3):
                search_map = {}

                for i in range(3):
                    for j in range(3):
                        if board[row+i][col+j] != "." and board[row+i][col+j] in search_map:
                            return False
                        search_map[board[row+i][col+j]] = True
        
        return True


        