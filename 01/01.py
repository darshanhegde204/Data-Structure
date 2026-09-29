num=int(input("Enter a Number: "))
flag=0
for i in range (2,(num//2)+1):
    if num%i==0:
        flag=flag+1
        break

if flag==1:
    print("Number is not prime")
else:
    print("Number is prime")
        