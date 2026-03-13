class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        sum_of_sub_array = sum(arr[:k])
        count=0
        if sum_of_sub_array/k >= threshold:
            count +=1


        for i in range(k,len(arr)):
            sum_of_sub_array = sum_of_sub_array+arr[i]-arr[i-k]
            if sum_of_sub_array/k >= threshold:
                count+=1
        
        return count

        