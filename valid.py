import string
x=input('Enetr password : ')
letters=[]
letters.extend(list(x))

letters_lower=(list(string.ascii_lowercase))
letters_upper=(list(string.ascii_uppercase))

num=['0','1','2','3','4','5','6','7','8','9']
character=['$','#','@']

l=0
u=0
n=0
c=0

for x in letters:
    for i in letters_lower:
        if x==i:
            l+=1
        else:
            continue

for x in letters:
    for i in letters_upper:
        if x==i:
            u+=1
        else:
            continue

for x in letters:
    for i in num:
        if x==i:
            n+=1
        else:
            continue

for x in letters:
    for i in character:
        if x==i:
            c+=1
        else:
            continue

if l==0:
    print("Lowercase character is missing")

elif u==0:
    print("Uppercase character is missing")

elif n==0:
    print("number from 1-9 is not in your password")

elif c==0:
    print("Choose a character from ($,#,@)")

elif len(letters)>16:
    print("Password is too large")

elif len(letters)<6:
    print("Password is too short")

else:
    print("Password is perfect")

# print(l,u,n,c)