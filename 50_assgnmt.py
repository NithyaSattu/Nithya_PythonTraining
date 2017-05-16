"""
input n=3 
    output: 	111
		101
		111
"""
num=input("Enter Number")
str1=''
for i in range(num):
    
    if i > 0 and i < num-1:
        str1 = "1" * num
        str1 = list(str1)
        for i in range(len(str1)):
            if i > 0 and i < len(str1)-1:
                str1[i] = "0"
        str1 = "".join(str1)
        print str1
    else:
        print "1" * num
