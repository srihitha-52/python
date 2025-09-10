def decToBin(num):
    str=''
    while num!=0:
        rem=num%2
        if rem==1:
            str+='1'
        else:
            str+='0'
        num=num//2
    return str[::-1]
a=int(input("enter a number:"))
print(decToBin(a))

