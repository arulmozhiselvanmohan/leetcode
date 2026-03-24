class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #box_index = (row // 3) * 3 + (col // 3)
        search_map = {}

        for row in range(0,len(board)):
            search_map = {}
            for col in range(0,len(board[row])):
                val = board[row][col]
                if val != "." and val in search_map:
                    return False
                search_map[val] = True
        
        
        for row in range(0,len(board)):
            search_map = {}
            for col in range(0,len(board[row])):
                val = board[col][row]
                if val !="." and val in search_map:
                    return False
                search_map[val] = True


        for row in range(0,len(board),3):
            for col in range (0, len(board),3):
                search_map = {}

                for i in range(3):
                    for j in range(3):
                        val = board[row+i][col+j]
                        if val != "." and val in search_map:
                            return False
                        search_map[val] = True
        
        return True


        