
x,y=map(int, input("Print oddd numbers in tha range of : ").split("-"))
print("number are : ")

for i in range(x,y):
    if i%5==0 and i%10==0:
        print(i)

    else:
        continue