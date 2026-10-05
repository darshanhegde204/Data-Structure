#Count:  Write a program to count vowels, consonants, digits and special characters in a given string.
strr=input("Enter a String: ")
v=0
c=0
d=0
sp=0
strr1=strr.lower()
for i in strr1:
    if i in ('a','e','i','o','u'):
        v+=1
    elif i in ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'):
        c+=1
    elif i in ('1','2','3','4','5','6','7','8','9','0'):
        d+=1
    else:
        sp+=1

print(f"Total vowels {v} , consonants {c} , digits {d} , special characters {sp} in string {strr}")