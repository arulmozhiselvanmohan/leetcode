class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        list_of_set = sorted(set(nums))
      
        count=1
        max_count=1

        for i in range(len(list_of_set)):
            if(i>0 and i<len(list_of_set)):
                if (list_of_set[i] == list_of_set[i-1]+1):
                    count +=1
                else:
                    count = 1

            max_count = max(max_count, count)
        
        return max_count
                    




        