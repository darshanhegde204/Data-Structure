n=int(input("Enter no of rows: "))
for i in range(n):
    print('  '*(n-i+1),end="")
    for j in range(2*i+1):
        print(chr(65+j), end=" ")
    print()