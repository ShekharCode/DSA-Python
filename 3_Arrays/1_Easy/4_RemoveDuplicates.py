ninput = lambda: int(input())
ainput = lambda: list(map(int, input().split()))


'''
# TC -> O(N)
def removeDuplicates(nums,n):
    st = set()
    for i in range(n):
        st.add(nums[i])
    k = len(st)
    return k
'''

# TC -> O(N)
def removeDuplicates(nums,n):
    # Write your code here.
    i = 0
    for j in range(1,n):
        if(nums[i]!=nums[j]):
            i+=1
            nums[i] = nums[j]    
    return i+1

if __name__ == "__main__":
    n = ninput()
    nums = ainput()
    k = removeDuplicates(nums,n)
    print(k)
    # for i in range(k):
    #     print(nums[i])

