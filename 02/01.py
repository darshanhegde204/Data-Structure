n=int(input("Enter no of rows: "))
for i in range(n):
    for j in range(i):
        print(chr(65+j), end=" ")
    print()