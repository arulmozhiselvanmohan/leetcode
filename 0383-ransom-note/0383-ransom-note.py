class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_map   = {};
        magazine_map = {};
        for char in ransomNote:
            if char in ransom_map:
                ransom_map[char] +=1
            else:
                ransom_map[char] = 1
        
        for char in magazine:
            if char in magazine_map:
                magazine_map[char] += 1
            else:
                magazine_map[char] = 1
        

        for key in ransom_map:
            if key in magazine_map:
                if ransom_map[key] > magazine_map[key]:
                    return False
                    break
            else:
                return False
        
        return True
        

            