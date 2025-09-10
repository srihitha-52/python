def binToDec(str):
    p2=1
    res=0
    n=len(str)-1
    for i in range(n,-1,-1):
        if str[i]=='1':
            res+=p2
        p2=p2*2
    return res
a=input("enter a binary number:")
print(binToDec(a))

    