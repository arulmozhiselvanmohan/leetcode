class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        
        for ast in asteroids:
                while result and ast < 0 < result[-1]:
                    if result[-1] < -ast:
                        result.pop()
                        continue
                    elif result[-1] == -ast:
                        result.pop()
                        break
                    else:
                        break              
                else:
                    result.append(ast)           
                    
        return result
