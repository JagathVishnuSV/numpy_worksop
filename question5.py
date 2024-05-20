#write a program to find if the given number is prime no or not
a=int(input("Enter a no:"))
flag=0
for i in range(2,int(a/2)):
    if i%a==0:
        flag=1
        break
    else:
        continue
print("Prime no" if flag==0 else "Not a prime no")