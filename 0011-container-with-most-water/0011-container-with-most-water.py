class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = int(len(height)-1)
        length = 0
        breadth = 0
        max_area = 0

        while(left<right):
            length = min(height[left],height[right])
            breadth = right - left
            current_area = length * breadth
            max_area = max(max_area, current_area)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1

        return max_area
            
        



            
                

                




        