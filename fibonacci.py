#fibonacci series
n=int(input("Enter number:"))
a=0
b=1

if n <= 0:
    print("enter positive number")

elif n==1:
    print(a)

else:
    print(a,b,end=" ")

for i in range(n-2):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
