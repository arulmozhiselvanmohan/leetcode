class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        i = 0

        while i < len(s):
            reversed_part = s[i:i+k][::-1]
            remaining_part = s[i+k:i+2*k]
            result += reversed_part + remaining_part
            i += 2 * k

        return result