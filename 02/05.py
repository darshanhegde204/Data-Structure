n=5
for i in range (n):
    if i==0 or i == n-1:
        for j in range (0,n):
            print("*",end=" ")
    else:
        for k in range (0,n):
            if k==0 or k==n-1:
                print("*" ,end=" ")
            else:
                print(" ", end=" ")
    print()