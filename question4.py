#given three integers,print the smallest one.(three integers should be user input)
A=int(input("Enter your 1st number :"))
B=int(input("Enter your 2nd number :"))
C=int(input("Enter your 3rd number :"))
if A<B<C:
    print(f"The smallest number is A: {A}")
elif B<A<C:
    print(f"the smallest number is B: {B}")
else:
    print(f"the smallest number is C: {C}")
