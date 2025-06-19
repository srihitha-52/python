def sumElements(arr):
    k=3
    n=len(arr)
    if n<=k:
        return 'invalid'
    count=0
    for i in range(n-k+1):
        if arr[i+1]==arr[i]+arr[i+2]:
            count+=1
    return count
nums=list(map(int,input("enter an array:").split(",")))
print(sumElements(nums))


