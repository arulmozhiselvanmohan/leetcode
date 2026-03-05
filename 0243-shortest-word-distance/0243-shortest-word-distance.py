class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1_idx = -1
        word2_idx = -1
        res = float('inf')

        for index, value in enumerate(wordsDict):
            if word1 == value:
                word1_idx = index
                if word2_idx != -1:
                    res = min(res,abs(word1_idx-word2_idx))
            elif word2 == value:
                word2_idx = index
                if word1_idx != -1:
                    res = min(res, abs(word1_idx-word2_idx))
        
        return res




        


        