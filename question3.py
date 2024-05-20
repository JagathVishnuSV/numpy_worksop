#write a program to find the factorial of a nummber
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter a no:--"))
print("Factorial=",fact(n))