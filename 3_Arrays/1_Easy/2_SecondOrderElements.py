ninput = lambda: int(input())
ainput = lambda: list(map(int, input().split()))

""""
# TC -> O(N*logN) -> Brute Force

def SecondOrderElements(nums,n):
    if n<2:
        return [-1,-1]
    nums.sort()
    return [nums[1],nums[n-2]]
"""

"""
#TC -> O(N) We do two linear traversals in our array -> Better Approach

def SecondOrderElements(nums,n):
    large = float('-inf')
    sLarge = float('-inf')
    small = float('inf')
    sSmall = float('inf')

    for num in nums:
        large = max(large,num)
        small = min(small,num)
    
    for num in nums:
        if (num > sLarge and num!=large):
            sLarge = num
        if(num < sSmall and num!=small):
            sSmall = num
    return [sSmall,sLarge]
"""


# TC -> O(N) -> Optimal Approach
def SecondSmallest(nums,n):
    small = float('inf')
    sSmall = float('inf')

    for num in nums:
        if num < small:
            sSmall = small
            small = num
        elif(num<sSmall and num!=small):
            sSmall = num
    return sSmall

def SecondLargest(nums,n):
    large = float('-inf')
    sLarge = float('-inf')

    for num in nums:
        if num>large:
            sLarge = large
            large = num
        elif (num>sLarge and num!=large):
            sLarge = num
    return sLarge


def SecondOrderElements(nums,n):
    sLargest = SecondLargest(nums,n)
    sSmallest = SecondSmallest(nums,n)
    return [sLargest,sSmallest]




n = ninput()
nums = ainput()
print(SecondOrderElements(nums,n))