# find if the given number is a palindrome or not?
n=input("Enter a no--")
if n==n[::-1]:
    print("palindrome")
else:
    print("not a palindrome")