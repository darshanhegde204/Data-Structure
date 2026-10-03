#Reverse the Array
arr=list(map(int,input("Enter array numbers after each number give space: ").split()))
resarr=[]
for i in range (len(arr)-1,-1,-1):
    resarr.append(arr[i])
print(resarr)