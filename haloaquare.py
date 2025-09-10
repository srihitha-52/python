def halosquare(n,m):
    for i in range(n):
        for j in range(m):
            if j==0 or j==(m-1) or i==0 or i== (n-1):
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()
n=int(input("enter no. of rows:"))
m=int(input("enter no. of columns:"))
halosquare(n,m)

            