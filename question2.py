"""write a program which accepts marks of four subject and displays total marks, percentage and grade"""
a=int(input("Enter your marks for Science:"))
b=int(input("Enter your marks for Maths:"))
c=int(input("Enter your marks for English:"))
d=int(input("Enter your marks for Social "))
total_marks=a+b+c+d
print(f"Total marks is {total_marks}")
Percentage=(a+b+c+d)*100/400
print(f"Your percentage is {Percentage} %")
if Percentage>60:
    print("you got A")
elif Percentage<40:
    print("You failed")
else:
    print("You got B")

