from sys import *
from collections import *
from math import *

ninput = lambda: int(input())
ainput = lambda: list(map(int, input().split()))

# O(NlogN) -> Brute Force
'''
def largestElement(nums:[],n:int) -> int:
    nums.sort()
    return nums[-1]
'''

#O(N) -> Optimal Approach
def largestElement(nums: [], n: int) -> int:

    # Write your code from here.
    maxi = nums[0]
    for num in nums:
        if(num>maxi):
            maxi = num
    return maxi

n = ninput()
nums = ainput()
print(largestElement(nums,n))