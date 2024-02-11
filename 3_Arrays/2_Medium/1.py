ninput = lambda: int(input())
ainput = lambda: list(map(int, input().split()))

def summation(arr,n):
    mul= 1
    for i in range(n):
        mul*=arr[i]
    return mul

n = ninput()
arr = ainput()
print(summation(arr,n))