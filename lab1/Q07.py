#Move Zeros to the End
arr=[0,5,3,0,1]
new=[]
zero=0
for num in arr:
    if num==0:
        zero+=1
    else:
        new.append(num)
for i in range (0,zero):
    new.append(0)
print(new)
