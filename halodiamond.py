def halodiamond(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ',end='')
        for k in range(2*i+1):
            if k==0 or k==2*i: 
                print("*",end='')
            else:
                print(" ",end='')
        print()
    #invert
    for i in range(n-2,-1,-1):
        for j in range(n-1-i):
            print(' ',end='')
        for k in range(2*i+1):
            if k==0 or k==2*i: 
                print('*',end='')
            else:
                print(' ',end='')
        print()
n=int(input("enter np. of rows:"))
halodiamond(n)
