def xInABox(n):
    for i in range(n):
        for j in range(n):
            if j==0 or i==0 or i==n-1 or j==n-1:
                print("*",end=' ')
            elif i==j or j==n-i-1:
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()  
n=int(input("enter no. of rows:"))
xInABox(n)
