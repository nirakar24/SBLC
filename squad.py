squad={}
squad_list=[]

n=int(input("Enter the no. of students : "))

for i in range(n):
    name=input("Enter your name : ")
    squad_list.append(name)
    temp=[]
    roll_no=int(input("Enter your roll no. : "))
    temp.append(roll_no)
    Course=input("Enter the course name : ")
    temp.append(Course)
    squad.update({f"{name}" : temp})

lst=list(squad.keys())
print()

for i in range(len(lst)):
    print(f" {i+1}.{lst[i]}")
x=int(input("\nPress index of the name whose data you want : "))


res_lst=squad[f"{squad_list[x-1]}"]

print()
print(f"Name : {squad_list[x-1]}")
print(f"Roll no : {res_lst[0]}")
print(f"Branch : {res_lst[1]}")
# print(squad)
