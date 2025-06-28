class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq_list = []

        for i in nums:
            sq_list.append(i ** 2)
        
        sq_list.sort()

        return sq_list