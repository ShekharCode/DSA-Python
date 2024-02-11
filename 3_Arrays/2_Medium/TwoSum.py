# O(N2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] +nums[j] == target:
                    ind.append(i)
                    ind.append(j)
        return ind


#O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i,num in enumerate(nums):
            nextNum = target - num
            if nextNum in dict:
                return [dict[nextNum],i]
            dict[num] = i
        return [] 
        