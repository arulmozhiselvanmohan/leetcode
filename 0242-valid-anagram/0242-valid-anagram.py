class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s)!=len(t)):
            return False
        
        S_dict = Counter(s)
        T_dict = Counter(t)

        #S_dict = {}
        #T_dict = {}

        #for char in s:
        #    if char in S_dict:
        #        S_dict[char] +=1
        #    else:
        #        S_dict[char] = 1
        
        #for char in t:
        #    if char in T_dict:
        #        T_dict[char] +=1
        #    else:
        #        T_dict[char] = 1

        return (S_dict == T_dict)
         

        
        