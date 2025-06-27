class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        stone_dict = {}
        result=0 

        for stone in stones:
            if stone in stone_dict:
                stone_dict[stone] += 1
            else:
                stone_dict[stone] = 1
        
        for jewel in jewels:
            if jewel in stone_dict:
                result += stone_dict[jewel]
        
        return result