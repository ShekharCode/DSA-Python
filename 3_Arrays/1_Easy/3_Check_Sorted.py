ninput = lambda: int(input())
ainput = lambda: list(map(int, input().split()))


# TC -> O(N2)
def isSorted(n,nums):
    for i in range(n):
        for j in range(i+1,n):
            if (nums[j]<nums[i]):
                return 0
    return 1

# TC -> O(N)
# def isSorted(n: int,  nums: [int]) -> int:
#     # Write your code here.
#     for i in range(n-1):
#         if nums[i+1] < nums[i]:
#             return 0
#     return 1

n = ninput()
nums = ainput()

print(isSorted(n,nums))