#O(n2)

def majorityElement(nums: [int]) -> int:
    # Write your code here
    n = len(nums)
    cnt = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if nums[i] == nums[j]:
                cnt+=1
        if cnt > (n//2):
            return nums[i]
    return -1

#O(N)

def majorityElement(nums: [int]) -> int:
    # Write your code here
    dictionary = {}
    n = len(nums)
    for num in nums:
        if num in dictionary:
            dictionary[num]+=1
        else:
            dictionary[num] = 1
    
    for num,cnt in dictionary.items():
        if cnt > (n//2):
            return num

#O(N) -> using Counter

from collections import Counter


def majorityElement(nums: [int]) -> int:
    # Write your code here
    counter = Counter(nums)
    n = len(nums)
    
    for num,cnt in counter.items():
        if cnt > (n//2):
            return num

# Moorve-Voting Algorithm
# O(N) 

def majorityElement(nums: [int]) -> int:
    # Write your code here
    el = None 
    cnt = 0

    for num in nums:
        if cnt == 0:
            el = num
            cnt = 1
        elif el == num:
            cnt+=1
        else:
            cnt-=1
    return el