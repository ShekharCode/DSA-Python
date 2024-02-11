from sys import *
from collections import *
from math import *

ninput = lambda: int(input())
ainput = lambda: list(map(int, input().split()))

'''
# TC -> O(N) SC -> O(N)
def rotateArray(arr,n):
    temp = [0]*n 
    for i in range(1,n):
        temp[i-1] = arr[i]
    temp[n-1] = arr[0]
    return temp
'''

# TC -> O(N) SC -> O(1)
def rotateArray(arr: [], n: int) -> []:
    # Write your code from here.
    val = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = val
    return arr

if __name__ == "__main__":
    n = ninput()
    nums = ainput()
    ans = rotateArray(nums,n)
    for num in ans:
        print(num)

