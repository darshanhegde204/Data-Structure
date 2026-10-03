#Remove Duplicate Elements
arr=[10,20,10,20,30,40]
newarr=[]
for num in arr:
    if num not in newarr:
        newarr.append(num)
print(newarr)
