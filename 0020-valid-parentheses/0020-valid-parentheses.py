class Solution:
    def isValid(self, s: str) -> bool:
        braces = []
        
         
        for i in range(len(s)):
            if s[i] == "{" or s[i] == "(" or s[i]== "[" :
                braces.append(s[i])
            else:
                if not braces:
                    return False
                if s[i] == "}":
                    if (braces[-1] != "{"):
                        return False
                    braces.pop()
                elif s[i] == ")":
                    if (braces[-1] != "("):
                        return False
                    braces.pop()
                elif s[i] == "]":
                    if (braces[-1] != "["):
                        return False
                    braces.pop()
        
        return len(braces)==0
                
