class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s)==len(t)):
            sorted_s_str = sorted(s)
            sorted_t_str = sorted(t)

            for i in range(len(sorted_s_str)):
                if(sorted_s_str[i] != sorted_t_str[i]):
                    return False
            
            return True
        
        else: 
            return False

        
        