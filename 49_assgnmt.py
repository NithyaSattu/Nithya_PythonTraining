"""
49. input = 1,2,3,4,5,6,8,10 output = odd,even,odd,even,odd,even,even,even

"""

a=input("Enter the numbers to find out even or odd")
b=[]


for i in a:
    if i%2==0:
        b.append("Even")
    else:
       b.append("Odd")
print a
print b
