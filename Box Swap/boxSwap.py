"""
BoxSwap

Description:
"""
a = float(input("Enter a number: "))
b = float(input("Enter a number: "))
print("Var a :",a)
print("Var b:", b)
if a < b:
    temp = a
    a = b
    b = temp
print("Var a :",a)
print("Var b:", b)