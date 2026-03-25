def move_array_to_right(n,k):
    b=len(n)
    c=b-k
    while c>0:
        a=n.pop(0)
        n.append(a)
        c-=1
    return n
n=list(map(int,input("Enter a list:").split(",")))
k=int(input("Enter number of positions to right:"))
print(move_array_to_right(n,k))