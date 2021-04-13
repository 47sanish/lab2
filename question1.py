#Check weather 5 is in the list of first 5 natural numbers or not.hint=list=>[1,2,3,4,5]
b=int(input("Enter your number:"))
a=[1,2,3,4,5]
if b in a:
    print(f"{b} is here")
else:
    print(f"sorry {b} isnt here")

