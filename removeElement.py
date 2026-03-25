def removeElement(nums,val):
    k=0
    for i in range(len(nums)):
        if nums[i]!=val:
            nums[k] = nums[i]
            k+=1
    return k
n=list(map(int,input("Enter a list:").split(",")))
v=int(input("Enter a number:"))
print(removeElement(n,v))