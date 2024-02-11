from sys import *
from collections import *
from math import *

ninput = lambda: int(input())
ainput = lambda: list(map(int, input().split()))


# Brute Force -> TC -> O(N) and sC -> O(N)
'''
def LeftRotateByK(nums,n,k):
    temp = [0]*k 
    for i in range(k):
        temp[i] = nums[i]
    for i in range(0,n-k):
        nums[i] = nums[i+k]
    for i in range(n-k,n):
        nums[i] = temp[n-k-i]
'''
# Optimal Approach -> TC -> O(N) and sC -> O(1) 
def reverse(nums,start,end):
    while(start <=end):
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start+=1
        end-=1

def leftRotateByK(nums,n,k):
    reverse(nums,0,k-1)
    reverse(nums,k,n-1)
    reverse(nums,0,n-1)
    print(nums)

n = ninput()
k = ninput()
nums = ainput()
leftRotateByK(nums,n,k)