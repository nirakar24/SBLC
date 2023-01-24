x=input('Enetr String : ')
letters=[]
letters.extend(list(x))

res=[]

no_of_letter=0

for i in letters:
    try:
        i=int(i)
        res.append(i)

    except ValueError as e:
        no_of_letter+=1

no_of_digits=len(res)

print(f"No. of digits in the given string are : {no_of_digits}")
print(f"No. of Letters in the given string are : {no_of_letter}")