class Solution:
    def isPalindrome(self, s: str) -> bool:

        if (s == ""):
            return True

        s2   = re.sub(r'[^a-zA-Z0-9]', '', s)
        test = s2.lower()

        left=0
        right=len(test)-1

        while(left<right):
            if(test[left] != test[right]):
                return False
            
            left +=1
            right -=1
        
        return True