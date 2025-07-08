class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        ref_search = []

        for row in range(len(matrix)):
            ref_search = set(matrix[row])
            if target in ref_search: 
                return True
        
        return False

        