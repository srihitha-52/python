def addPrime(num):
    a={2,3,5,7}
    sum=0
    while num!=0:
        digit=num%10
        if digit in a:
            sum+=digit
        num=num//10
    return sum
b=int(input("enter a number:"))
print(addPrime(b))

