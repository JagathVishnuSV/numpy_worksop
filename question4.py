#write a program to find the sum of digits of a given number'
n=int(input("Enter a no:--"))
sum=0

while(n>0):
    rem=n%10
    sum=sum+rem
    n//=10
print(sum)