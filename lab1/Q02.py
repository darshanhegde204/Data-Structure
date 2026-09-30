#Find the smallest and Largest Element:
arr=list(map(int,input("Enter the Numbers of the array and after each number give a space: ").split()))
#print(arr)
lar=arr[0]
lar2=0
sml=arr[0]
sml2=0
n=len(arr)
for i in range(n):
    if arr[i]>lar:
        lar2=lar
        lar=arr[i]
    elif arr[i]>lar2 and arr[i]!=lar:
        lar2=arr[i]

    if arr[i]<sml:
        sml2=sml
        sml=arr[i]
    elif arr[i]<sml2 and arr[i]!=sml:
        sml2=arr[i]
    
print(lar)
print(lar2)
print(sml)
print(sml2)