def plusOne(digits):
    a=int("".join(str(x) for x in digits))
    a+=1
    a=[int(d) for d in str(a)]
    return a
digits=list(map(int,input("Enter a list:").split(",")))
print(plusOne(digits))