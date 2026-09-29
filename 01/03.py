n=int(input("Enter a number: "))
sum=0
num=n
while(num>0):
    sum=sum*10+(num%10)
    num=num//10
if (n==sum):
    print(True)