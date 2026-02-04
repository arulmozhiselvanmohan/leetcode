class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram = {}

        for index, value in enumerate(strs):
            pattern = "".join(sorted(value))

            if pattern in anagram:
                anagram[pattern].append(value)
            else:
                anagram[pattern] = [value]
        
        return list(anagram.values())

       

        
                

        