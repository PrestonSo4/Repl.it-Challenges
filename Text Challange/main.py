"""
Challenge

Description:
"""
#\\\\Challenge 1\\\\#
"""
for i in range(1,10):
    print("#"*i)"""
def hill():
    h = int(input("Enter the height of the hill: "))
    for i in range(1,h+1):
        print("#"*i)
hill()
#-------------------#
#\\\\Challenge 2\\\\#
"""
spaces = 18
for i in range(1,10):
    spaces -= 2
    y = ("#"*i)+(" "*spaces)+("#"*i)
    print(y)
"""
def cave():
    height = int(input("Enter the height of the cave: "))
    for i in range(1,height+1):
        print(("#"*i)+(" "*(((height)-i)*2)+("#"*i)))
        # Can you simpily the above even more? 
        # Once you find a way to simplify cave(), then simplify cross() & diamond()

cave()     
#-------------------#
#\\\\Challenge 3\\\\#
"""
space1 = 6
space2 = 0
for i in range(1,5):
    print((space2*" ") + ("#") + (" "*space1) + ("#") + (space2*" ")) 
    space2 += 1
    space1 -= 2

space1 = 0
space2 = 3
for i in range(1,5):
    print((space2*" ") + ("#") + (" "*space1) + ("#") + (space2*" ")) 
    space2 -= 1
    space1 += 2
"""
def cross():
    h = int(input("Enter the height of the cross: "))
    for i in range(1 if h % 2 == 0 else 0, int(h/2 + 1 if h % 2 == 0 else int(h/2))):
        print((" "*i)+ "#"+ " "*((int(h/2)-i)*2) + "#"+ (" "*i))
    print(" "*i + " ##") if h % 2 != 0 else i * 1
    for i in reversed(range(1 if h % 2 == 0 else 0, int(h/2 + 1 if h % 2 == 0 else int(h/2)))):
        print((" "*i)+ "#"+ " "*((int(h/2)-i)*2) + "#"+ (" "*i))
         

cross()     
#-------------------#
#\\\\Challenge 4\\\\#
"""
space =  5
for i in range(1,10,2):
    print((space * " ")+ (i*"#") +(space * " "))
    space -= 1
space =  2
y = 7
for i in range(1,10,2):
    print((space * " ")+ (y*"#") +(space * " "))
    space += 1
    y -= 2
"""
def diamond():
    height = int(input("Enter the height you want the diamond to be: "))
    height = (int(height/2)+1) if height % 2 != 0 else (int(height/2))
    for i in range(1,height*2, 2):
        print(" "*int(height-(i/2)) + "#"*i )
    for i in reversed(range(1, height*2 if height % 2 == 0 else height*2 -2,2)):
        print(" "*int(height-(i/2)) + "#"*i )
diamond()


                

#-------------------#