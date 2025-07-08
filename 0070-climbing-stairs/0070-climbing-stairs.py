class Solution:
    def climbStairs(self, n: int) -> int:
        fib = [0] * (n+2)
        fib[0] = 0
        if n>0:
            fib[1] = 1

            for i in range(2,n+2):
                fib[i] = fib[i-2] + fib[i-1]
        
        return fib[n+1]