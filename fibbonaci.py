n=int(input("Enter the length of fibonacci series : "))

a=0
b=1
print("Series : ")
for i in range(n):
    if n<0:
        print("Invalid input")
    
    elif n==0:
        print(0)
    
    elif n==1:
        print(1)

    else:
        c=a+b
        a=b
        b=c
        print(b)
