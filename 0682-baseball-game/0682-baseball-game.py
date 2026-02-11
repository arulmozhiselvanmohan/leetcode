class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []
        
        for i in operations:
            if i=="C":
                if(points):
                    points.pop()
            elif i=="D":
                if(points):
                    points.append(2 * points[-1])
            elif i=="+":
                if (len(points) >=2):
                    points.append(points[-1]+points[-2])
                elif len(points) == 1:
                    points.append(points[-1])
                else:
                    points.append(0)
            else:
                points.append(int(i))
        
        return(sum(points))
