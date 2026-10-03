#Count Even and Odd Numbers:
arr=list(map(int,input("Enter the element of array after each element give a space: ").split()))
even=0
odd=0
for i in arr:
    if i%2==0:
        even+=1
    else :
        odd+=1
print(f"There are {even} even and {odd} odd element in this array")