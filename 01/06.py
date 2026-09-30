n=int(input("Enter a number of rows: "))

for i in range (n,0,-1):
    for j in range(i,0,-1):
        print(j, end=" ")
    print()