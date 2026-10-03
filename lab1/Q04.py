#Search an Element
num=int(input("Enter the number you want to search: "))
arr=[2,4,9,6,0,1]
res=0
ind=0
for i in range(0,len(arr)):
    if arr[i] == num:
        res=1
        ind=i
if res==1:
    print(f"Number {num} found at Index {ind}")
else:
    print(f"Number {num} is Not found")

