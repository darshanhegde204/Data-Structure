#Calculate Array Sum:
n = int(input("Enter the number of elements (N): "))
arr=input(f"Enter {n} numbers after each number give space: ").split()
new_arr=list(map(int,arr))
total=0
for i in range (0,len(new_arr)):
    total=total+new_arr[i]

print(total)