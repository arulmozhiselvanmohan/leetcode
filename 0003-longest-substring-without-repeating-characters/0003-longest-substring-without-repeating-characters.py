class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        if not s:
            return 0


        start=0
        end=1
        storage = {s[0]}
        length = 1

        while(end < len(s)):
            if(s[end] not in storage):
                storage.add(s[end])
                length = max(length, len(storage))
                end+=1
            else:
                storage.remove(s[start])
                start+=1
        
        return length
