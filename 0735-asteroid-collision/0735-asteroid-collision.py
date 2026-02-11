class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        
        for ast in asteroids:
                #Explodes only when top of stack is positive and asteriod is negative
                while result and ast < 0 < result[-1]:
                    if result[-1] < -ast:
                        result.pop()
                        # top of stack explodes
                        continue
                    elif result[-1] == -ast:
                        result.pop()
                        #Both explode
                        break
                    else:
                        # asteroid explodes
                        break              
                else:
                    result.append(ast)           
                    
        return result
